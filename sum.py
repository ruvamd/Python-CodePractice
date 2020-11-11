def sum2(nums):

#alternative code
  #return sum(nums[:2])

  if len(nums)==0:
    return 0
  elif len(nums)<2:
    return nums[0]
  else:
      return sum(nums[:2])

print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))