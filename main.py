from flows.statsFlow import StatsFlow

welcome = "***WELCOME TO PHYSIOSTATS***\n\nChoose one of the following:\n"
menu = "\n1. new\n2. load\n3. delete\n4. help\n5. exit\n\n"

def processMenu():
    print("Inside menu")

def main():
    flow = StatsFlow()
    while True:
        entry = input("PhysioStats> ")
        if entry == "new" or entry == "1":
            flow.new()
        elif entry == "load" or entry == "2":
            pass
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
