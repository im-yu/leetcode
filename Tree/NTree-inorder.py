"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def dfs(root,depth):
            if root:
                if len(res) <= depth:
                    res.append([])
                res[depth].append(root.val)
                for child in root.children:
                    dfs(child,depth+1)
        dfs(root,0)
        return res