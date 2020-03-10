# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(node):
            if not node:return 0
            R = depth(node.right)
            L = depth(node.left)
            self.ans = max(self.ans,L+R)
            return max(L,R)+1
        depth(root)
        return self.ans