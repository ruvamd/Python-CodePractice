class tree_node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def max_depth(self,root):
        if root is None:
            return 0
        return 1+max(self.max_depth(root.left),self.max_depth(root.right))

if __name__=="__main__":
    root=tree_node(3)
    root.left=tree_node(9)
    root.right=tree_node(20)
    root.right.left=tree_node(15)
    root.right.right=tree_node(7)
    print(Solution().max_depth(root))