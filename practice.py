nmrLst=[4, 5, 1, 8]
trg=9

class solution(object):
    def twoSum(self,nums,target):
        hashTable={}
        for i in range(len(nums)):
            result=target-nums[i]
            if result in hashTable:
                return [hashTable[result],i]
            else: hashTable[nums[i]]=i
print(solution().twoSum(nmrLst,trg))






























# class solution(object):
#     def twoSum(self,nums,target):
#         hashTable={}
#         for i in range(len(nums)):
#             result=target-nums[i]
#             if result in hashTable:
#                 return [hashTable[result],i]
#             else: hashTable[nums[i]]=i
# print(solution().twoSum(nmrLst,target))
