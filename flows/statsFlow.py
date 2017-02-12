from repositories.statsRepository import StatsRepository

class StatsFlow:

    def __init__(self):
        self.repository = StatsRepository()

    def index(self):
       fileNames = self.repository.getAll()
       counter = 0
       for fileName in fileNames:
           if counter < 10:
               counter += 1
           else:
               entry = input("Press 'ENTER' for more or 'b' to break.")
               if entry == 'b':
                   break
               else:
                   counter = 0
           print(fileName)

    def new(self):
        print("\nInput name of file. Press 'c' to cancel.\n")
        while True:
            fileName = input("name: ")
            if self.repository.existsFile(fileName):
                print("\nFile already exists. Try something else or exit by pressing 'c'.\n")
            elif fileName != '':
                break
        if fileName == "c":
            print("\n")
            return
        self.repository.addFile(fileName)
        self.repository.save(fileName)
        print("\nCongratulations a new file named " + fileName + ".csv has been created.\n")