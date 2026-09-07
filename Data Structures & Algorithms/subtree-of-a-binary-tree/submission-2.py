# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(r, sub):
            if not r and not sub:
                return True
            if r and sub and r.val == sub.val:
                return same(r.left, sub.left) and same(r.right, sub.right) 
            return False

        if not subRoot:
            return True 
        elif not root:
            return False
        elif same(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
