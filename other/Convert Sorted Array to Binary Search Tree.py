from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    print(Solution().sortedArrayToBST(nums))

'''solution 2: prints with nulls'''
# from typing import List, Optional
# from collections import deque

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def serialize_bst(root: TreeNode) -> List[int]:
#     serialization = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         if node:
#             serialization.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             serialization.append(None)
#     return serialization

# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         if not nums:
#             return None
#         mid = len(nums) // 2
#         root = TreeNode(nums[mid])
#         root.left = self.sortedArrayToBST(nums[:mid])
#         root.right = self.sortedArrayToBST(nums[mid+1:])
#         return root

# if __name__ == "__main__":
#     nums = [-10,-3,0,5,9]
#     root = Solution().sortedArrayToBST(nums)
#     serialized = serialize_bst(root)
#     print(serialized)



    
    


    
