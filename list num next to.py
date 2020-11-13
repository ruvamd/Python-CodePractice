
"""
Given an array of ints, return True if the array contains 
a 2 next to a 2 somewhere. 
"""

def has22(nums):
  for i,v in enumerate(nums[:-1]):
    if v == 2 and nums[i+1] == 2:
      return True
  return False

print(has22([1, 2, 2])) #→ True
print(has22([1, 2, 1, 2])) #→ False
print(has22([2, 1, 2])) #→ False