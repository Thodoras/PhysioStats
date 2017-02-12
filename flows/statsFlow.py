from repositories.statsRepository import StatsRepository

class StatsFlow:

    def __init__(self):
        self.repository = StatsRepository()

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
        self.repository.saveFile(fileName)
        self.repository.save(fileName)
        print("\nCongratulations a new file named " + fileName + ".csv has been created.\n")