from repositories.indexRepository import IndexRepository


class IndexFlow:

    def __init__(self):
        self.repository = IndexRepository()

    def index(self):
        file_names = self.repository.get_all()
        counter = 0
        for file_name in file_names:
            if counter < 10:
                counter += 1
            else:
                entry = input("Press 'ENTER' for more or 'b' to break.")
                if entry == 'b':
                    break
                else:
                    counter = 0
            print(file_name)

    def new(self):
        print("\nInput name of file. Press 'c' to cancel.\n")
        while True:
            file_name = input("name: ")
            if self.repository.exists(file_name):
                print("\nFile already exists. Try something else or exit by pressing 'c'.\n")
            elif file_name != '':
                break
        if file_name == "c":
            print("\n")
            return
        self.repository.insert(file_name)
        print("\nCongratulations a new file named " + file_name + ".csv has been created.\n")

    def exists(self, file_name):
        if self.repository.exists(file_name):
            print("\nYou chose to configure " + file_name + "\n")
            return True
        print("\nFile does not exist. Press 's' to show available files or 'b' to go back to main menu.\n")
        return False
