from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left,root.right)
        
    def isMirror(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val==right.val and self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)

if __name__=="__main__":
    root=TreeNode(1)
    root.right=TreeNode(2)
    root.left=TreeNode(2)
    root.left.left=TreeNode(3)
    root.left.right=TreeNode(4)
    root.right.left=TreeNode(4)
    root.right.right=TreeNode(3)
    print(Solution().isSymmetric(root))
        