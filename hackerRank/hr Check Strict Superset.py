a=set(input().split())

for _ in range(int(input())):
    r=a.issuperset(set(input().split()))
print(r)

#print(all(a > set(input().split()) for _ in range(int(input()))))