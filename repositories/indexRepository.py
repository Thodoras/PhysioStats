from repositories.repository import *


class IndexRepository(Repository):

    INDEX = "/index.csv"

    def get_all(self):
        with open(self.fullPath(self.INDEX), 'r') as f:
            file_names = []
            reader = csv.reader(f)
            for row in reader:
                file_names.append(row[0])
            return file_names

    def exists(self, file_name):
        with open(self.fullPath(self.INDEX), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0 and row[0] == file_name:
                    return True
        return False

    def insert(self, file_name):
        with open(self.fullPath(self.INDEX), 'a+') as f:
            writer = csv.writer(f)
            writer.writerow([file_name])
        self._initialize_file(file_name)

    def _initialize_file(self, file_name):
        with open(self.fullPath("/" + file_name + ".csv"), 'a+') as f:
            writer = csv.writer(f)
