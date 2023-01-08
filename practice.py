class tree_node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def inorder_traversal(self,root):
        if root is None:
            return []
        return self.inorder_traversal(root.left)+[root.val]+self.inorder_traversal(root.right)

if __name__=="__main__":
    root=tree_node(1)
    root.right=tree_node(2)
    root.left=tree_node(3)
    print(Solution().inorder_traversal(root))


