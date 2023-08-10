
#result with index,class
# i is index,nums[i] is number from nums list

# :type nums: List[int]
# :type target: int
# :rtype: List[int]

nmrLst=[4,5,1,8]
trg=9

class solution:
    def twoSum(self,nums,target):
        hashTable={}
        for i in range(len(nums)):
            result=target-nums[i]
            if result in hashTable:
               return [hashTable[result],i]
               #print([hashTable[result],i])
            else: hashTable[nums[i]]=i

print(solution().twoSum(nmrLst,trg))
#solution().twoSum(nmrLst,trg)

'''
#---result with numerals---#

# Driver Code
numArr = [4, 5, 1, 8]
pairSum = 9  

def twoSumHashing(numArr, pairSum):
   sums = []
   hashTable = {}
   for i in range(len(numArr)):
      result=pairSum-numArr[i]
      if result in hashTable:
         print(f'Because {result}+{numArr[i]}=={pairSum},we return{result,numArr[i]}')
         #print([result,numArr[i]])
      else: hashTable[numArr[i]]=numArr[i]  
  
# Calling function
twoSumHashing(numArr, pairSum)
'''

#--two for loops--#
#use return and call function to return one pair of indexes 
nmrLst=[4,5,1,8]
trg=9
def bruteForceTwoSum(nums,target):
   for i in range(len(nums)):
      for j in range(i+1,len(nums)):
         sum=nums[i]+nums[j]
         if sum==target:
            #return [i,j] #one index result
            #print([i,j])  #two index result
            print(nums[i],nums[j])
#print(bruteForceTwoSum(nmrLst,trg)) #one index result
bruteForceTwoSum(nmrLst,trg) #two index result
