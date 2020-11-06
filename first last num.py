def first_last6(nums):
    return 6 in [nums[0],nums[-1]]

#alternative code
    # n=nums[0],nums[-1]
    # if 6 in n:
    #    return True
    # return False

print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))
