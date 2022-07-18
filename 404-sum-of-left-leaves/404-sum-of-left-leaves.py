# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def traversal(root):
            temp = 0
            if root == None:
                return temp
            
            if root.left and root.left.left == None and root.left.right == None:
                temp += root.left.val
            return temp + traversal(root.left) + traversal(root.right)
            
        Sum = traversal(root)
        return Sum
        