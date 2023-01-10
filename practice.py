class Tree_node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def sorted_array_to_bst(self,nums):
        if not nums:
            return None
        mid=len(nums)//2
        root=Tree_node(nums[mid])
        root.left=self.sorted_array_to_bst(nums[:mid])
        root.right=self.sorted_array_to_bst(nums[mid+1:])
        return root
    
if __name__=="__main__":
    nums=[-10,-3,0,5,9]
    print(Solution().sorted_array_to_bst(nums))

