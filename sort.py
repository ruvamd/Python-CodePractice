p=[0,-10,15,-2,1,12]
s=sorted(p)
print(s)

coffee=['Starbucks','peets','green']
print(sorted(coffee))
print(sorted('My favorite coffee is Peets'.split(),key=str.upper))

leaderBoard={231:'ckl',123:'abc',432:'jkc'}
print(sorted(leaderBoard,reverse=True))

students=[('alise','b',16),('bobby','a',18),('mary','c',17)]
print(sorted(students,key=lambda student:student[2]))