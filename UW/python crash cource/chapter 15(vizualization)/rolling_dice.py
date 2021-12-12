from random import randint

class Die:
    def __init__(self):
        self.num_sides=6

    def roll(self):
        return randint(1,self.num_sides)

