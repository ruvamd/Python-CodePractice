# nOfstdEn=input()
# rollNstdEn=set(input().split())
# nOfstdFr=input()
# rollNstdFR=set(input().split())
# print(len(rollNstdEn|rollNstdFR))
# print(rollNstdEn|rollNstdFR)

#---alt code---
m,n=[set(input().split()) for _ in range(4)][1::2]
print(len(m&n))
print(m&n)
