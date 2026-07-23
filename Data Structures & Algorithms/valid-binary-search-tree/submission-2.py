# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            if not root.left and not root.right:
                return True
            if root.left and root.left.val >= root.val:
                return False
            elif root.right and root.right.val <= root.val:
                return False
            else: 
                if root.left and root.right:
                    return self.isValidBST(root.left) and self.isValidBST(root.right)
                elif root.left:
                    return self.isValidBST(root.left)
                else:
                    return self.isValidBST(root.right)
        else:
            return False
