class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=23
    
    def get_descriptive_name(self):
       long_name=f'{self.make} {self.model} {self.year}'
       return long_name
    
    def read_odometer(self):
        print(f'the odometer for the used car is {self.odometer}')
    
    def update_odometer(self,milage):
        if milage>=self.odometer:
            self.odometer=milage
        else:print("you can't roll back odometer")
    
    def increment_odometer(self,miles):
        self.odometer+=miles

# my_new_car=Car('bmw','m5',2005)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.odometer=23
# my_new_car.read_odometer()
# my_new_car.update_odometer(25)
# my_new_car.read_odometer()

used_car=Car('subaru','m1','2016')
print(used_car.get_descriptive_name())

used_car.update_odometer(23000)
used_car.read_odometer()

used_car.increment_odometer(100)
used_car.read_odometer()
