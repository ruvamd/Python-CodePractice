class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1

x = 8
print(Solution().mySqrt(x))

'''using with math''' 
# from math import sqrt,floor

# def mySqrt(x):
#     x=sqrt(x)
#     return floor(x)

# x=8
# print(mySqrt(x))