#n is number of students subsribed to english and french newsletter
#s is list of student roll numbers who have subscribed to the English andFrench newspaper
n,s=[set(input().split()) for _ in range(4)][1::2]
print(len(n^s))
print(n^s)

#---alt code---
m,n=[set(input().split()) for _ in range(4)][1::2]
print(*sorted(m^n,key=int),sep='\n')
