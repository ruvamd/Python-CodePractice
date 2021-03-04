from collections import namedtuple

#---alt code---
# students=5
# #ID,MARKS,NAME,CLASS=names
# name=['Raymond','Steven','Adrian','Stewart','Peter']
# marks=[97,50,91,72,80]
# avr=sum(marks)/students
# print(avr)

#---alt code---
n, Score = int(input()) , namedtuple('Score',input().split())
scores = [Score(*input().split()).MARKS for i in range(n)]
print("%.2f"% (sum(map(int,scores))/n))

# n=int(input())
# score=namedtuple('score'.input().split())



# n, Student = int(input()), namedtuple('Student', input())
# print("{:.2f}".format(sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n))

# for id in range(1,students+1):
#     for m in id:
#         print(m)
# cl=int[7,4,9,5,6]

# colors=nt('color',['red','green','blue'])
# col=colors(55,155,255)
# print(col.red)
