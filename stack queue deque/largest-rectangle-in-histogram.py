class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights =  heights +[0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res