class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]

solution = Solution()

print(solution.isPalindrome("racecar"))  # Output: True
print(solution.isPalindrome("hello"))    # Output: False
print(solution.isPalindrome("madam"))    # Output: True
print(solution.isPalindrome("Able was I ere I saw Elba"))  # Output: True
