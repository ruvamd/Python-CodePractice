import random
dishwasher=['a','b','c']
for dish in list(dishwasher):
    if not random.randint(0,2):
        print('out of space')
        break
    else:
        print(f'putting {dish} in the cabinet')
        dishwasher.remove(dish)