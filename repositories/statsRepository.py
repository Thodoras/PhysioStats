import os
import csv

class StatsRepository:

    DIR =  os.path.dirname(__file__)
    DATA = "../data"
    INDEX = "/index.csv"

    def getAll(self):
        with open(self._fullPath(StatsRepository.INDEX), 'r') as f:
            fileNames = []
            reader = csv.reader(f)
            for row in reader:
                fileNames.append(row[0])
            return fileNames

    def existsFile(self, fileName):
        with open(self._fullPath(StatsRepository.INDEX), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0 and row[0] == fileName:
                    return True
        return False

    def addFile(self, fileName):
        with open(self._fullPath(StatsRepository.INDEX), 'a+') as f:
            writer = csv.writer(f)
            writer.writerow([fileName])

    def save(self, fileName, modelList = []):
        if modelList == []:
            self._initializeFile(fileName)

    def _fullPath(self, relativePath):
        return os.path.join(StatsRepository.DIR, StatsRepository.DATA + relativePath)

    def _initializeFile(self, fileName):
        with open(self._fullPath("/" + fileName + ".csv"), 'a+') as f:
            writer = csv.writer(f)