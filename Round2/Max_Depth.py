# Given the root of a binary tree, return its depth.

# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:



# Input: root = [1,2,3,null,null,4]

# Output: 3
# Example 2:

# Input: root = []

# Output: 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = deque([root])
        level = 0

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1

        return level

## Iterative DFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, level = stack.pop()

            if node:
                res = max(res, level)
                stack.append([node.left, level+1])
                stack.append([node.right, level+1])

            
        return res


