import os

class Option:
    def __init__(self, name, fun):
        self.name = name
        self.fun = fun

    def use(self):
        self.fun()


class Menu:
    index = 0
    options = []

    def show_options(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i, option in enumerate(self.options):
            if i == self.index:
                print(">", option.name)
            else:
                print(option.name)

    def move_down(self):
        self.index += 1
        if self.index > len(self.options) - 1:
            self.index = 0
        self.show_options()

    def move_up(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.options) - 1
        self.show_options()

    def interact(self):
        self.options[self.index].use()