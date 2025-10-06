"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        mapping = {}

        def dfs(node):
            if node in mapping:
                return mapping[node]
            
            copy = Node(node.val)
            mapping[node] = copy
            # we go through every neighbour and it intilizes as we find connected nodes
            # this relies on the graph being connected
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        return dfs(node) if node else None