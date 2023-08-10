import random

decider=random.randrange(2)

if decider==0:
    print('heads')
else:
    print('tails')
    
print(decider)
print('you rolled a '+str(random.randrange(1,7)))

lotteryW=random.sample(range(100),5)
print(lotteryW)
