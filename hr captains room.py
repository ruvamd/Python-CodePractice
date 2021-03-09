# g=int(input())
# a=set(input().split())
# n='8'
# if n in a:
#     print(n)

s=sorted([input().split() for _ in range(2)][1])
print((set(s[0::2])^set(s[1::2])).pop())
