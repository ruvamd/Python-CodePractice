from random import randint
class Die:
    def __init__(self):
        self.sides=20
        
    def roll_die(self):
        for d in range(11):
            random_number=randint(1,self.sides)
            print(random_number)
        # return random_number

ran_num=Die()
ran_num.roll_die()

#output
6
18
10
11
11
16
1
5
8
12
13