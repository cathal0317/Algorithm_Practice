# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Example 1:



# Input: root = [1,2,3,4,5,6,7]

# Output: [1,3,2,7,6,5,4]
# Example 2:



# Input: root = [3,2,1]

# Output: [3,1,2]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            cur = queue.popleft()
            cur.left, cur.right = cur.right, cur.left

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root

        
