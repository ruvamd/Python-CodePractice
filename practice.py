from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the current and maximum subarray sums
        current_sum = max_sum = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Calculate the current sum by choosing the larger of the current element
            # or the current element combined with the current subarray sum
            current_sum = max(nums[i], current_sum + nums[i])

            # Update the maximum subarray sum if the current sum is larger
            max_sum = max(max_sum, current_sum)

        return max_sum
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
print(sol.maxSubArray(nums))