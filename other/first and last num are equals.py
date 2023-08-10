'''Given an array of ints, return True if the array is length 1 or more, 
and the first element and the last element are equal.'''

def same_first_last(nums):
    return 1>=1 and nums[0]==nums[-1]

#alternative code1
    # if len(nums)>=1 and nums[0]==nums[-1]:
    #     return True
    # return False

#alternative code2    
    # n=1
    # if n>=1 and nums[0]==nums[-1]:
    #  return True 
    # return False
print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([1, 2, 1]))