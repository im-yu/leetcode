#
# sum = []
# res = []
# pro =[]
# for i in range(100):
#     for j in range(100):
#         for k in range(100):
#             if i * j * k == 36:
#                 if i >= j and j >= k:
#                     num = i + j + k
#                     pro.append([i,j,k])
#                     if num in sum:
#                         res.append([i, j, k])
#                     else:
#                         sum.append(num)
# print(pro)
# print(res)

class Solution:
    def trap(self, height: List[int]) -> int:
        cur = 0
        stack = []
        while cur < len(height):
            while stack != [] and  height[cur] > height[stack[-1]]:
                h = height[stack[-1]]
                stack.pop()
                if stack == []:
                    break
            distance = cur - stack[-1] -1
            min_ = min(height[cur],height(stack[-1]))
            sum_ = sum_ + distance * (min_ - h)
        stack.append(cur)
        cur += 1
        return sum_





