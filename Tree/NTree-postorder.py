"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def pre(root):
            if root:
                res.append(root.val)
                for child in reversed(root.children):
                    pre(child)
        pre(root)
        return res[::-1]
