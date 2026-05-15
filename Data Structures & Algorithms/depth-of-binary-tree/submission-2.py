# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        else:
            q = [root]
            curr_length = 1
            max_depth = 0
            while q:
                print(len(q))
                curr_length = len(q)
                max_depth +=1 
                for i in range(curr_length):
                    curr = q.pop(0)
                    if curr is not None:
                        if curr.left is not None:
                            q.append(curr.left)
                        if curr.right is not None:
                            q.append(curr.right)
            
            return max_depth
