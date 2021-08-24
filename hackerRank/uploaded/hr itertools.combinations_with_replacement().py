'''
input: HACK 2
'''
from itertools import combinations_with_replacement as cwr

s,n=(input().upper()).split()

for i in cwr(sorted(s),int(n)):
    print(''.join(i))
'''
output:
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''