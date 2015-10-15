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

    # def complete(self):
    #     return False

    def run(self):
        print('run')
        

        #unzip ndocs
        print((os.path.join(base.BEEHOME,self.train_dir+'/*')))
        images = [x for x in glob.glob(os.path.join(base.BEEHOME,self.train_dir+'/*'))]
        #print(images)
        #images  = map(lambda x: img_to_matrix(x),images)
        images = [img_to_matrix(x) for x in images[0:10]]
          

        data = []
        for i,image in enumerate(images):

            img = flatten_image(image)
            print(img[1:5])

            print(img.shape)
            data.append(img)

        # data = np.array(data)

        print(data[0].shape)



        pca = RandomizedPCA(n_components=2)

        X = pca.fit_transform(data)

        print(X.shape)
        df = pd.DataFrame({"x": X[:, 0], "y": X[:, 1]}) #, "label":np.where(y==1, "check", "driver's license")})
        colors = ["red", "yellow"]
        #for label, color in zip(df['label'].unique(), colors):
        for color in colors:
            plt.scatter(df['x'], df['y'], c=color) 
            #plt.scatter(df[mask]['x'], df[mask]['y'], c=color) #, label=label)
        plt.legend()
        plt.show()




if __name__ == '__main__':
    luigi.run()
