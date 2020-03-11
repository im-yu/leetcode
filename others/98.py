# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node,compare_1 = float('-inf'),compare_2 = float('inf')):
            if not node:
                return True
            val = node.val
            if val <= compare_1 or val >= compare_2:
                return False
            if not helper(node.right,val,compare_2):#node.right是第二层的左子树
                return False
            if not helper(node.left,compare_1,val):#node.left是第二层的右子树
                return False
            return True
        return helper(root)