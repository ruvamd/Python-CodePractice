class tree_node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def is_symmetric(self,root):
        if root is None:
            return True
        return self.is_mirror(root.left,root.right)

    def is_mirror(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val==right.val and self.is_mirror(left.left,right.right) and self.is_mirror(left.right,right.left) 

if __name__=="__main__":
    root=tree_node(1)
    root.right=tree_node(2)
    root.left=tree_node(2)
    root.left.left=tree_node(3)
    root.left.right=tree_node(4)
    root.right.left=tree_node(4)
    root.right.right=tree_node(3)
    print(Solution().is_symmetric(root))


