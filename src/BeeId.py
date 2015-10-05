from gluish.task import BaseTask
import luigi
import luigi.mock
import time
import pandas as pd
import networkx as nx
from settings import base

class ImageNorm(BaseTask):

    ndocs = luigi.IntParameter(default=10)
    test_dir = luigi.Parameter(default='./test')
    train_dir = luigi.Parameter(default='./train')

    def complete(self):
        return False

    def run(self):
        print('run')
        

        #unzip ndocs
        images = [x for x in glob.glob(self.train)]
        print(images)
        #normalize one at a time

        #save somewhere