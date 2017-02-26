from repositories.statsRepository import StatsRepository


class StatsFlow:

    def __init__(self):
        self.repository = StatsRepository()

    def new(self, file_name):
        data = [0, 0, 0, 0]
        not_completed = True
        while not_completed:
            print("\nInput data.Press 'c' to cancel or x to restart.\n")
            for i in range(4):
                self._print_right_add_message(i)
                input_data = input("input data: ")
                if input_data == 'c':
                    return
                elif input_data == 'x':
                    break
                else:
                    data[i] = input_data
                    if i == 3:
                        self.repository.new(data, file_name)
                        not_completed = False
                        print("\nFile successfully updated\n")

    def _print_right_add_message(self, index):
        if index == 0:
            print("Input an id for the row, e.g. kilos to calculate")
        else:
            print("Input no. " + str(index) + " data.")