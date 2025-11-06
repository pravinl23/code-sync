# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            return [str(root.val)]
        def traverse(path, node):
            if not node:
                return
            if not node.left and not node.right:
                res.append(path + "->" + str(node.val))

            if path is None:
                traverse(str(node.val), node.left)
                traverse(str(node.val), node.right)
            else:
                traverse(path + "->" + str(node.val), node.left)
                traverse(path + "->" + str(node.val), node.right)

        traverse(None, root)
        return res