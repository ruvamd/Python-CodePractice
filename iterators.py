import itertools
for x in itertools.count(50,5):
    print(x)
    if x==80:
        break

x=0
for c in itertools.cycle(['recap',1,'qwerty',2]):
    print(c)
    x+=1
    if x>50:
        break

for r in itertools.repeat(True):
    print(r)
    x+=1
    if x>80:
        break