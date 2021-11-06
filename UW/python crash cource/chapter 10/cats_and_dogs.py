try:
    with open('UW/python crash cource/chapter 10/cats.tx') as f:
        data_cats=f.read()
except FileNotFoundError:
    # print('the cats.txt not found')    
    pass
else:
    print(data_cats)
try:
    with open('UW/python crash cource/chapter 10/dogs.txt') as f:
        data_dogs=f.read()
except FileNotFoundError:
    print('the dogs.txt not found')     
else:
    print(data_dogs)