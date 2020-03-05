# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)
            else:return
        postorder(root)
        return res

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.right
            else:
                tmp = stack.pop()
                root = tmp.left
        return res[::-1]