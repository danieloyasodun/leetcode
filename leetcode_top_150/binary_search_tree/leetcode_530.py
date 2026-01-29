# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        prev = [None]  # use list to hold prev
        res = [float("inf")]  # use list to hold res

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if prev[0]:
                res[0] = min(res[0], node.val - prev[0].val)
            prev[0] = node
            dfs(node.right)

        dfs(root)
        return res[0]
