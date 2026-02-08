# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queuep = deque([p])
        queueq = deque([q])
        if len(queuep) != len(queueq):
            return False
        while queuep and queueq:
            for _ in range(len(queuep)):
                nodep = queuep.popleft()
                nodeq = queueq.popleft()

                if nodep is None and nodeq is None:
                    continue
                if nodep is None or nodeq is None or nodep.val != nodeq.val:
                    return False
                else:
                    queuep.append(nodep.left)
                    queuep.append(nodep.right)
                    queueq.append(nodeq.left)
                    queueq.append(nodeq.right)
        return True







