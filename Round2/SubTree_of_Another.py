# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:



# Input: root = [1,2,3,4,5], subRoot = [2,4,5]

# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False
        
        if self.dfs(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

        

    def dfs(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val == node2.val:
            return self.dfs(node1.left,node2.left) and self.dfs(node1.right,node2.right)

        return False

    
