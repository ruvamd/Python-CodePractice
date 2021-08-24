'''
input:
6
append 1
append 2
append 3
appendleft 4
pop
popleft
'''
from collections import deque
d=deque()

for _ in range(int(input())):
    method, *n = input().split()
    getattr(d, method)(*n)

#---alt code---
#     cmd, *args = input().split()
#     getattr(d, cmd)(*args)
# [print(x, end=' ') for x in d]

#---alt code---
    # s = input().split()
    # if s[0]=="append":
    #     d.append(s[1])
    # elif s[0]=="appendleft":
    #     d.appendleft(s[1])
    # elif s[0]=="pop":
    #     d.pop()
    # elif s[0]=="popleft":
    #     d.popleft()
print(*d)
'''
output: 1 2
'''