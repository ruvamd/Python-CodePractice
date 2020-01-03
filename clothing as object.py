class jeans:
    def __init__(self,waist,length,color):
        self.waist=waist
        self.length=length
        self.color=color
        self.wearing=False
    def putOn(self):
        print(f'Putting on {self.waist}x{self.length} {self.color} jeans')
        self.wearing=True
    def takeOff(self):
        print(f'taking off {self.waist}x{self.length} {self.color} jeans')
        self.wearing=False