import os
import csv


class Repository:

    DIR = os.path.dirname(__file__)
    DATA = "../data"

    def fullPath(self, relative_path):
        return os.path.join(self.DIR, self.DATA + relative_path)