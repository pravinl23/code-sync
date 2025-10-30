# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(node, counter):
            if not node:
                return
            if counter == len(res):
                res.append([])
            res[counter].append(node.val)
            dfs(node.left, counter + 1)
            dfs(node.right, counter + 1)
        
        dfs(root, 0)
        return res