class vehicle:
    name=''
    kind='car'
    color=''
    value=100.00
    def description(self):
        desc_str=f'{self.name} is a {self.kind} {self.color} worth {self.value}'
        return desc_str

car=vehicle
car1,car2=car()

def car():
    car.name=input('Enter the name of the car: ')
    car.kind=input('Enter kind of the car: ')
    car.color=input('Enter the color of the car: ')
    car.value=input('Enter the value of the car: ')
if car1==car2:
    print(car)

    


