from repositories.repository import *


class StatsRepository(Repository):

    INDEX = "/index.csv"

    def new(self, data, file_name):
        with open(self.fullPath('/' + file_name + '.csv'), 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)