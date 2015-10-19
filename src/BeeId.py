from gluish.task import BaseTask
import luigi
import luigi.mock
import time
import pandas as pd
from settings import base
import glob
import os
from BeeId_helper import img_to_matrix, flatten_image
from sklearn.decomposition import RandomizedPCA
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


class ImageNorm(BaseTask):

    seed = luigi.Parameter(default=1)
    ndocs = luigi.IntParameter(default=10)
    test_dir = luigi.Parameter(default='test')
    train_dir = luigi.Parameter(default='train')
    train_label = luigi.Parameter(default='train_labels.csv')

    # def complete(self):
    #     return False

    def run(self):
        print('run')
        

        #unzip ndocs
        print((os.path.join(base.BEEHOME,self.train_dir+'/*')))
        image_files = [x for x in glob.glob(os.path.join(base.BEEHOME,self.train_dir+'/*'))]
        #print(images)
        #images  = map(lambda x: img_to_matrix(x),images)
        images = [(x,img_to_matrix(x)) for x in image_files[0:100]]

        label_df = pd.read_csv(os.path.join(base.BEEHOME, self.train_label))

        data = []
        for i,image_tuple in enumerate(images):

            image_f,image = image_tuple
            #image is np array of 3-element tuples


            #we can reduce the colorspace and or filter


            #we can flatten each color - we
            r,g,b = zip(*image)

            imgN  = image_f.split('.')[-2]
            imgN = np.int(imgN.split('/')[-1])
            
            img = {'imgN':imgN,'r':r,'g':g,'b':b,'label':(label_df[label_df.id==imgN]).genus}

            #print(len(r))


            #img = flatten_image(r)

            data.append(img)

        # data = np.array(data)

        #print(data)

        pca = RandomizedPCA(n_components=2)


        # in the future peform a more intellent color reduction/aggregation
        just_r = [x['r'] for x in data]


        data = just_r
        X = zip(pca.fit_transform(data),[x['label'] for x in data])

        print(X[0])


        # grab some labels
        print(os.path.join(base.BEEHOME,self.train_label))
        label_df = pd.read_csv(os.path.join(base.BEEHOME, self.train_label))

        print(label_df.head())


        #df = pd.DataFrame({"x": X[:, 0], "y": X[:, 1]}, "label":np.where(y==1, "check", "driver's license")})
        colors = ["red", "yellow"]
        #for label, color in zip(df['label'].unique(), colors):
        for color in colors:
            plt.scatter(df['x'], df['y'], c=color)
            #plt.scatter(df[mask]['x'], df[mask]['y'], c=color) #, label=label)
        plt.legend()
        plt.show()




if __name__ == '__main__':
    luigi.run()
