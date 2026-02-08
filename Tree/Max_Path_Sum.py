# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

# The path sum of a path is the sum of the node's values in the path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            res[0] = max(res[0], root.val + leftmax + rightmax)
            return root.val + max(rightmax,leftmax)
        dfs(root)
        return res[0]

            

            

            
        


        