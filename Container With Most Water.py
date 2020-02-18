# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         maxArea=0
#         for i in range(len(height)-1):
#             for j in range(i+1,len(height)):
#                 Area=(j-i)*min(height[i],height[j])
#                 maxArea=max(maxArea,Area)
#         return maxArea
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(height)-1
        while i < j:
            Area = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, Area)
            if height[i] > height[j]:
                j -=1
            else:
                i +=1
        return maxArea
