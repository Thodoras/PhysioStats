from flows.statsFlow import StatsFlow

welcome = "***WELCOME TO PHYSIOSTATS***\n\nChoose one of the following:\n"
menu = "\n1. new\n2. load\n3. delete\n4. help\n5. exit\n\n"

def load(flow):
    print("\nInsert file name or press 's' to show available files or 'b' to go back to main menu\n")
    while True:
        fileName = input("\nFile name: ")
        if fileName == 'b':
            return
        elif fileName == 's':
            flow.index()
        elif fileName != '':
            pass

def processMenu():
    print("Inside menu")

def main():
    flow = StatsFlow()
    while True:
        entry = input("PhysioStats> ")
        if entry == "new" or entry == "1":
            flow.new()
        elif entry == "load" or entry == "2":
            load(flow)
        elif entry == "delete" or entry == "3":
            pass
        elif entry == "help" or entry == "4":
            print(menu)
        elif entry == "exit" or entry == "5":
            print("\nBye!\n")
            break
        else:
            print("Invalid input. Press 'help' to print menu options.")

print(welcome)
print(menu)
main()
