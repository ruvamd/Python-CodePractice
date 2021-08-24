'''
input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
'''
for i in range(int(input())):
    for _ in range(int(input())):
        a=set(input().split())
    for _ in range(int(input())):
        b=set(input().split())
    print(a.issubset(b))

# for i in range(int(input())):
#     _, a = input(), set(map(int, input().split()))
#     _, b = input(), set(map(int, input().split()))
#     print(a.issubset(b))       
'''
output:
True 
False
False
'''