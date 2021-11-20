from random import randint,choice

class Lottery:
    def __init__(self):
        self.ran_list=[1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']

    def ran_num_let(self):
        for _ in range(4):
            ran_n_l=choice(self.ran_list)
            print(f'every match number and letter will win {ran_n_l}')

lottery=Lottery()
lottery.ran_num_let()