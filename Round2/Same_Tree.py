# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Example 1:



# Input: p = [1,2,3], q = [1,2,3]

# Output: true
# Example 2:



# Input: p = [4,7], q = [4,null,7]

# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            nodep, nodeq = stack.pop()

            if not nodep and not nodeq:
                continue
            if not nodep or not nodeq or nodep.val != nodeq.val:
                return False
            
            stack.append((nodep.right, nodeq.right))
            stack.append((nodep.left, nodeq.left))
        
        return True

            