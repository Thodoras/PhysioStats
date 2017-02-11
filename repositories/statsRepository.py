import os
import csv

class StatsRepository:

    DIR =  os.path.dirname(__file__)
    DATA = "../data"
    INDEX = "/index.csv"

    def existsFile(self, fileName):
        with open(self._fullPath(StatsRepository.DATA + StatsRepository.INDEX), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == fileName:
                    return True
        return False

    def saveFile(self, fileName):
        with open(self._fullPath(StatsRepository.DATA + StatsRepository.INDEX), 'w') as f:
            writer = csv.writer(f)
            writer.writerow([fileName])

    def save(self, modelList):
        pass

    def _fullPath(self, relativePath):
        return os.path.join(StatsRepository.DIR, relativePath)