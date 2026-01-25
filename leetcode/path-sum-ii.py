# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        res = []
        def backtrack(node, path, total):
            if not node:
                return

            path.append(node.val)
            total += node.val
            
            # base case
            if not node.left and not node.right and total == targetSum:
                res.append(path[:])
            
            backtrack(node.left, path, total)
            backtrack(node.right, path, total)

            path.pop()
                
        

        backtrack(root, [], 0)
        return res