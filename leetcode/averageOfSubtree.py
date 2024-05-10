from typing import Optional, List
from binarytree import TreeNode


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return (0, 0)
            
            # Recursively traverse left and right subtrees
            left_count, left_sum = dfs(node.left)
            right_count, right_sum = dfs(node.right)
            
            # Calculate the count and sum for the current subtree
            subtree_count = 1 + left_count + right_count
            subtree_sum = node.val + left_sum + right_sum
            
            # Calculate the average for the current subtree and convert it to an integer
            subtree_average = int(subtree_sum / subtree_count)
            
            # Append the average to the result list
            result.append(subtree_average)
            
            return (subtree_count, subtree_sum)
        
        result = []  # To store averages of each subtree
        dfs(root)
        
        return result
        
root = [4,8,5,0,1,None,6]
print(Solution().averageOfSubtree(root))