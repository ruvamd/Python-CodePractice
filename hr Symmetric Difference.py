m,n=[set(input().split()) for _ in range(4)][1::2]
print(*sorted(m^n,key=int),sep='\n')
