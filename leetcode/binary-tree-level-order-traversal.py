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
        NodeMap = {}
        
        def dfs(node, counter):
            if not node:
                return
            if counter not in NodeMap:
                NodeMap[counter] = []
            NodeMap[counter].append(node.val)
            if node.left:
                dfs(node.left, counter + 1)
            if node.right:
                dfs(node.right, counter + 1)
        
        dfs(root, 0)

        res = []
        for item in NodeMap:
            res.append(NodeMap[item])

        return res