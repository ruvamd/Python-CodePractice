from ast import List
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - i - 1))
        num += 1
        return [int(i) for i in str(num)]


digits = [1,2,3]
print(Solution().plusOne(digits))