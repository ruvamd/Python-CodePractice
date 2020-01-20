class car:
    pass
class truck(car):
    pass
c=car()
convert=car()
t=truck()
print(type(c)==type(t))
print(type(c)==type(convert))
print(isinstance(c,car))
print(isinstance(t,truck))