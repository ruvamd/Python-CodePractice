# nums=[2,7,11,15]
# target=9

# for i in range(len(nums)):
#     a=i+i
#     if a==target:
#         print(a.index())
    

'''
class Solution(object):
   def twoSum(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
      required = {}
      for i in range(len(nums)):
         if target - nums[i] in required:
            return [required[target - nums[i]],i]
         else:
            required[nums[i]]=i
input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))
'''

# Driver Code
num_arr = [4, 5, 1, 8]
pair_sum = 9  

def twoSumHashing(num_arr, pair_sum):
    sums = []
    hashTable = {}

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            print("Pair with sum", pair_sum,"is: (", num_arr[i],",",complement,")")
        hashTable[num_arr[i]] = num_arr[i]  
  
# Calling function
twoSumHashing(num_arr, pair_sum)
