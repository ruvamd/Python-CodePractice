import random
dirty=True
scrubCount=0

while(dirty):
    scrubCount+=1
    print(f'scrub the pan: {scrubCount}')
    print('rinse&check if the pan is clean')
    if not random.randint(0,9):
        print('all clean!')
        dirty=False
    else:
        print('still dirty...')
