from itertools import combinations_with_replacement as cwr

s,n=(input().upper()).split()

for i in cwr(sorted(s),int(n)):
    print(''.join(i))
