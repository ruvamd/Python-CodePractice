# numOfStdEn=input()
# rollNumOfStdEn=set(input().split())
# numOfStdFr=input()
# rollNumOfStdFr=set(input().split())
# print(len(rollNumOfStdEn & rollNumOfStdFr))
# print(rollNumOfStdEn & rollNumOfStdFr)

numOfStdL,rollNumOfStdL=[set(input().split()) for _ in range(4)][1::2]
print(len(numOfStdL&rollNumOfStdL))
print(numOfStdL&rollNumOfStdL)