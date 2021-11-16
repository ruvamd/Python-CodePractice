class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def sit(self):
        print(f'{self.name} sit')
    def roll_over(self):
        print(f'{self.name} roll over')

my_dog=Dog('willie',6)
print(f'\nmain dog name is {my_dog.name} and age {my_dog.age}')
my_dog.sit()
my_dog.roll_over()

your_dog=Dog('dasy',9)
print(f'\nyour dog name is {your_dog.name} and age {your_dog.age}')
your_dog.sit()
your_dog.roll_over()