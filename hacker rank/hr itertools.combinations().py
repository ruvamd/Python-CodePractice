from itertools import combinations as cm
s,n=input().split()

for i in range(1,int(n)+1):
    for j in cm(sorted(s),i):
        print(''.join(j))
