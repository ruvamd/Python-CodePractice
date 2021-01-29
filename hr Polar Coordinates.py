import cmath as c

#---alt code---
# n=complex(1,2)
# f=c.polar(n)
# print(f)

#---alt code 1---
# r=int(input())
# ph=int(input())
# comp=complex(r,ph)
# convert=c.polar(comp)
# print(*convert,sep='\n')

print(*c.polar(complex(input())),sep='\n')

#---alt code 2---
# comp=complex(input())
# convert=c.polar(comp)
# print(*convert,sep='\n')
