import random

playerP=260
attackLowPoint=60
attackHighPoint=80

while playerP>0:
    dmg=random.randrange(attackLowPoint,attackHighPoint)
    playerP=playerP-dmg
    if playerP<=30:
        playerP=30
    print(f'Enemy strike for {dmg} points of damage.Current HP is {playerP}')
    if playerP==30:
        print('You have low health.')
        break