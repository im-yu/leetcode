# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
            else:return
        preorder(root)
        return res

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            else:
                tmp = stack.pop()
                root = tmp.right
        return res