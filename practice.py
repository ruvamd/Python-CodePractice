class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            return x == x[::-1]

x=121
print(Solution().isPalindrome(x))