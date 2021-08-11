'''
enter:
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
'''
a=set(input().split())

for _ in range(int(input())):
    r=a.issuperset(set(input().split()))
print(r)
#print(all(a > set(input().split()) for _ in range(int(input()))))

#output: False