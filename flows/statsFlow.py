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

    def add(self, fileName):
        data = [0, 0, 0, 0]
        notCompleted = True
        while notCompleted:
            print("\nInput data.Press 'c' to cancel or x to restart.\n")
            for i in range(4):
                self._printRightAddMessage(i)
                inputData = input("input data: ")
                if inputData == 'c':
                    return
                elif inputData == 'x':
                    break
                else:
                    data[i] = inputData
                    if i == 3:
                        self.repository.add(data, fileName)
                        notCompleted = False
                        print("\nFile successfully updated\n")

    def existsFileName(self, fileName):
        if self.repository.existsFile(fileName):
            print("\nYou chose to configure " + fileName +"\n")
            return True
        print("\nFile does not exist. Press 's' to show available files or 'b' to go back to main menu.\n")
        return False

    def _menu(self, fileName):
        print(StatsFlow.MENU)

    def _printRightAddMessage(self, index):
        if index == 0:
            print("Input an id for the row, e.g. kilos to calculate")
        else:
            print("Input no. " + str(index) + " data.")