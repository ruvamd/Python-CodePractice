n=range(int(input()))
names=set()
for _ in n:
    cn=input()
    names.add(cn)  
print(len(names))

#---alt code---
# print(len(set([str(input()) for x in range(int(input()))])))

#---alt code---
# s=set()
# for _ in range(int(input())):
#     s.add(input())
# print(len(s))