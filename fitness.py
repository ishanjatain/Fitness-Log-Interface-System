import sys

class ActivityNote:
    def _init_(self, work_name, mins_used, kcal_val, day_tag):
        self.work = str(work_name).strip().lower()
        self.day = day_tag

        try:
            self.mins = float(mins_used)
            self.kcal = int(kcal_val)
        except:
            print("Numbers were not valid. Resetting to 0.")
            self.mins = 0.0
            self.kcal = 0

    def show(self):
        return f"{self.work.capitalize()} for {self.mins} minutes, {self.kcal} Kcal on {self.day}"


class RecordBox:
    def _init_(self):
        self.items_list = []

    def push(self, item):
        self.items_list.append(item)

    def get_total(self):
        total_k = 0
        for one in self.items_list:
            total_k += one.kcal
        return total_k


def menu_screen():
    print("=== FITNESS TRACK MENU ===")
    print("1. Add Activity")
    print("2. Total Calories")
    print("3. Show All")
    print("9. Quit")


def ask_inputs():
    nm = input("Activity name: ")
    mn = input("Minutes spent: ")
    kc = input("Calories: ")
    dy = input("Date (YYYY-MM-DD): ")
    return nm, mn, kc, dy


def launcher():
    box = RecordBox()

    while True:
        menu_screen()
        opt = input("Choose option: ")

        if opt == "1":
            raw = ask_inputs()
            rec = ActivityNote(*raw)
            box.push(rec)
            print("Added:", rec.day)

        elif opt == "2":
            t = box.get_total()
            print("Total calories burned:", t)
            if t > 0:
                print("#" * (t // 50))

        elif opt == "3":
            print("--- Records ---")
            for x in box.items_list:
                print(x.show())

        elif opt == "9":
            print("Closing app.")
            sys.exit()

        else:
            print("Invalid selection, try again.")

launcher()