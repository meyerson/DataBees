from gluish.task import BaseTask
import luigi
import luigi.mock
import time
import pandas as pd
from settings import base
import glob
import os
from BeeId_helper import img_to_matrix


class ImageNorm(BaseTask):

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

        img_to_matrix(images[0])

        #normalize one at a time

        #save somewhere

if __name__ == '__main__':
    luigi.run()
