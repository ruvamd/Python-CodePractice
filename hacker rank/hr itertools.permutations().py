from itertools import permutations

# s=input().split()
# str,n=sorted(s[0]),int(s[1])

# print(*list(map(''.join,permutations(str,n))),sep='\n')

#---alt code---
# s,n = input().split()
# print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')

#---alt code---
word,num=input().split(' ')
permutations=list(permutations(word,int(num)))
permutations.sort()
for i in permutations:
    print(''.join(i))

