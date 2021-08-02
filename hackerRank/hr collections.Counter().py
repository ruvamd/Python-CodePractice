from collections import Counter
'''
enter:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''
x=int(input()) #number of shoes
stkSzs=Counter(map(int,input().split())) #sizes in stock
totalRevenue = 0
for _ in range(int(input())):
    size,price = map(int,input().split())
    if stkSzs[size]:
        totalRevenue+=price
        stkSzs[size]-=1

print(totalRevenue)

# output: 200