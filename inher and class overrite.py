class vehicle:
    def __init__(self,color,manuf):
        self.color=color
        self.manuf=manuf
        self.gas=4
    def drive(self):
        if self.gas>0:
            self.gas-=1
            print(f'the {self.color} {self.manuf} goes VROOOM!')
        else:
            print(f'the {self.color} {self.manuf} sputters out of gas.')
class car(vehicle):
    def radio(self):
        print('rocking tunes!')
    def window(self):
            print('ahhh... fresh air!')
class motorcycle(vehicle):
    def helmet(self):
        print('nice and save!')
class ecar(car):
    def drive(self):
            print(f'the {self.color} {self.manuf} goes ssshhh!')