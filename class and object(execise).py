class vehicle:
    name=''
    kind='car'
    color=''
    value=100.00
    def description(self):
        desc_str=f'{self.name} is a {self.kind} {self.color} worth {self.value}'
        return desc_str

car1=vehicle()
car1.name=input('Enter the name of the car: ')
car1.kind=input('Enter kind of the car: ')
car1.color=input('Enter the color of the car: ')
car1.value=input('Enter the value of the car: ')
print('\nThe second car enter next.\n')
car2=vehicle()
car2.name=input('Enter the name of the car: ')
car2.kind=input('Enter kind of the car: ')
car2.color=input('Enter the color of the car: ')
car2.value=input('Enter the value of the car: ')

print(car1.description())
print(car2.description())
