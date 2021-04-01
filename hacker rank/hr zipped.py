nStd,xStd=map(int,input().split())
scores=[map(float,input().split()) for _ in range(xStd)]
for std in zip(*scores):
    print(sum(std)/xStd)

# a,y = map(int, input().split())
# scores = [map(float, input().split()) for _ in range(y)]
# [print(sum(student)/y) for student in zip(*scores)]

#---alt code---
# n, x = map(int, input().split()) 
# sheet = []
# for _ in range(x):
#     sheet.append(map(float,input().split())) 
# for i in zip(*sheet): 
#     print(sum(i)/len(i))
