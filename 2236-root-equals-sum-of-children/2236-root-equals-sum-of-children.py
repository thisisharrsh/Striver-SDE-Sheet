# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        lval = 0 
        rval = 0
        if(root==None or (root.left==None and root.right == None)):
            return True
        else:
            if(root.left!=None):
                ldata=root.left.val
            if(root.right!=None):
                rdata = root.right.val 
            if(root.val==rdata+ldata and (self.checkTree(root.right) and self.checkTree(root.left))):
                return True
            
            else:
                return False
        