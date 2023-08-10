from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        if not nums1:
            nums1 = nums2
            return
        if not nums1 and not nums2:
            return
        if m == 0:
            nums1[:] = nums2[:]
            return
        if n == 0:
            return
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
                m += 1
        if j < n:
            nums1[i:] = nums2[j:]
        return

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)

'''second solution'''
# def merge(nums1, m, nums2, n):
#         pointer = len(nums1) - 1
#         m = m - 1
#         n = n - 1
        
#         while m >= 0 and n >= 0:

#             if nums1[m] >= nums2[n]:
#                 nums1[pointer] = nums1[m]
#                 m -= 1

#             else:
#                 nums1[pointer] = nums2[n]
#                 n -= 1
                
#             pointer -= 1
            
#         if n >= 0:
#             nums1[:n+1] = nums2[:n+1]

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# merge(nums1, m, nums2, n)
# print(nums1)
