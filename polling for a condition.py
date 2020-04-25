import time

hungry=True
while(hungry):
    print('opening the front door')
    frontDoor=open('frontDoor.txt','r')
    if 'pizza guy' in frontDoor:
        print('pizza is here!')
        hungry=False
    else:
        print('not yet...')
    print('closing the front door')
    frontDoor.close()
    time.sleep(1)
