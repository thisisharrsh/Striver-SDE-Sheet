# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        que = []
        res=[]
        que.append(root)
        
        while(len(que)>0):
            res1 = []
            for i in range(len(que)):
                Node = que.pop(0)
                res1.append(Node.val)
                
                if Node.left is not None:
                    que.append(Node.left)
                if Node.right is not None:
                    que.append(Node.right)
            res.append(res1)
                
                
        return res
             
        