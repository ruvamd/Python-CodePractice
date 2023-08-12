from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        triangle = [[1]]  # Initialize with the first row
        
        for i in range(1, numRows):
            prev_row = triangle[i - 1]
            new_row = [1]
            
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
            
            new_row.append(1)
            triangle.append(new_row)
        
        return triangle

solution = Solution()

numRows = 5
print(solution.generate(numRows))
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

numRows = 1
print(solution.generate(numRows))
# Output: [[1]]
