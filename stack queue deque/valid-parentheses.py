class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'[':']','{':'}','(':')','?':'?'}
        stack = ['?']
        for i in s:
            if i in dic:stack.append(i)
            elif dic[stack.pop()] != i:
                return False
        return len(stack) == 1

