class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        target = sum(A)/3
        if sum(A) % 3 != 0:
            return False
        n = len(A)
        i,cur = 0,0
        while i < n:
            cur += A[i]
            if cur == target:
                break
            i += 1
        if cur != target: return False
        j = i+1
        while j < n-1:
            cur += A[j]
            if cur == target*2:
                return True
            j += 1
        return False

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True