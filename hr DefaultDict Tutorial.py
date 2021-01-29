from collections import defaultdict

n=3 #int(input('enter the length:'))
m=2 #int(input('enter the amount:'))
d=defaultdict(list)
for i in range(n):
    d[input('enter the letters:')].append(i+1)
for i in range(m):
    print(*d[input('enter the letter to count:')] or [-1])

#---alt code---
# from collections import defaultdict

# # Inputs
# # ------
# n, m = map(int, input().split(' '))

# # Let's get the groups as lists
# # -----------------------------
# #input1 = ['a', 'a', 'b', 'a', 'b']
# #input2 = ['a', 'b']
# input1 = list()
# for i in range(n):
#     input1.append(input())

#     input2 = list()
# for i in range(m):
#     input2.append(input())

# # Calculate Output
# # ----------------
# d = defaultdict(list)

# # Fill d with input1 values
# for i in range(n):
#     d[input1[i]].append(i+1)
# #print(d) --> defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]})

# # Apply the logic for printing
# for i in input2:    
#     if i in d:
#         print(*d[i])
#     else:
#         print(-1)

#--example--
# s = 'mississippi'
# d = defaultdict(int)
# for k in s:
#     d[k] += 1

# sorted(d.items())
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

# print(f,s,groupA,groupB)