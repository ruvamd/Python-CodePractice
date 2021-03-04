n=int(input())
s=set(map(int,input().split()))
N=int(input())

for i in range(N):
    string = input().split()
    if string[0] == 'pop':
        s.pop()
    elif string[0] == 'remove':
        s.remove(int(string[1]))
    elif string[0] == 'discard':
        s.discard(int(string[1]))

#for _ in range(N):
#---alt code---
    # attr,*num=map(str,input().split())
    # getattr(s,attr) (*(int(x) for x in num))

#---alt code    
    # attr,*kw=input().split()
    # if kw:
    #     getattr(s,attr)(*(map(int,*kw)))
    # else:getattr(s,attr)()
#---alt code---
    # eval('s.{0}({1})'.format(*input().split()+['']))
    
print(sum(s))