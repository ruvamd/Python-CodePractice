'''
Given an array of ints length 3, figure out which is larger, the first or 
last element in the array, and set all the other elements to be that value. 
Return the changed array.
'''
def max_end3(nums):
    if nums[0]>nums[-1]:
        return [nums[0]]*3
    elif nums[0]<nums[-1]:
        return [nums[-1]]*3
    else: nums[0]==nums[-1]
    return [nums[0]]*3

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))
print(max_end3([2, 4, 2]))
