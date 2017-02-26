from flows.statsFlow import StatsFlow
from flows.indexFlow import IndexFlow

WELCOME = "***WELCOME TO PHYSIOSTATS***\n"
MENU = "\nMAIN MENU\n\n1. new\n2. load\n3. delete\n4. menu\n5. exit\n\n"
FILE_MENU = "\n1. show all rows\n2. show specific row\n3. add\n4. update row\n5. delete row\n6. menu\n7. back\n\n"


def load(index_flow):
    print("\nInsert file name or press 's' to show available files or 'b' to go back to main menu\n")
    while True:
        fileName = input("\nFile name: ")
        if fileName == 'b':
            return
        elif fileName == 's':
            index_flow.index()
        elif fileName != '':
            if index_flow.exists(fileName):
                processMenu(index_flow, fileName)
                break


def processMenu(index_flow, fileName):
    print(FILE_MENU)
    stats_flow = StatsFlow()
    while True:
        entry = input("PhysioStats\\" + fileName + "> ")
        if entry == "show all rows" or entry == "1":
            pass
        elif entry == "show specific row" or entry == "2":
            pass
        elif entry == "add" or entry == "3":
            stats_flow.new(fileName)
        elif entry == "update row" or entry == "4":
            print(FILE_MENU)
        elif entry == "delete row" or entry == "5":
            print(FILE_MENU)
        elif entry == "menu" or entry == "6":
            print(FILE_MENU)
        elif entry == "back" or entry == "7":
            print(MENU)
            break
        else:
            print("Invalid input. Press 'menu' to print menu options.")

def main():
    index_flow = IndexFlow()
    while True:
        entry = input("PhysioStats> ")
        if entry == "new" or entry == "1":
            index_flow.new()
        elif entry == "load" or entry == "2":
            load(index_flow)
        elif entry == "delete" or entry == "3":
            pass
        elif entry == "menu" or entry == "4":
            print(MENU)
        elif entry == "exit" or entry == "5":
            print("\nBye!\n")
            break
        else:
            print("Invalid input. Press 'menu' to print menu options.")

print(WELCOME)
print(MENU)
main()
