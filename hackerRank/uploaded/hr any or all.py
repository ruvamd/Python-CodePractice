'''
input: 
5
12 9 61 5 14 
'''
nRange=input()
numbers=list(map(int,input().split()))
print(all([x>0 for x in numbers]) and any([str(x)==str(x)[::-1] for x in numbers]))

# N = int(input())
# integers = input().split()
# if all(int(i) >= 0 for i in integers):
#     if any(num == num[-1:] for num in integers):
#         print("True")
# else:print("False")
'''
output: True
'''

