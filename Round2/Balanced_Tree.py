# Given a binary tree, return true if it is height-balanced and false otherwise.

# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:



# Input: root = [1,2,3,null,null,4]

# Output: true
# Example 2:



# Input: root = [1,2,3,null,null,4,null,5]

# Output: false
# Example 3:

# Input: root = []

# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return [True, 0]
            
           
            left, right = dfs(node.left), dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 
            return [balanced, 1+ max(left[1], right[1])]

        return dfs(root)[0]