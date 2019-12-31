f=5
#print(f)

#f='hi'
#print(f)

#print('hi'+str('123'))

def someFunction():
    global f
    f='def'
    print(f)
someFunction()
print(f)

del f
print(f)