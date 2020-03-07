def L_sum(List):
    sum = 0
    for i in List:
        sum = sum + i
    return sum
sum = []
res = []
pro =[]
for i in range(100):
    for j in range(100):
        for k in range(100):
            if i * j * k == 36:
                if i >= j and j >= k:
                    num = i + j + k
                    pro.append([i,j,k])
                    if num in sum:
                        num_36 = num
                    else:
                        sum.append(num)
for i in pro:
    if L_sum(i) == num_36:
        res.append(i)
print(res)

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         cur = 0
#         stack = []
#         while cur < len(height):
#             while stack != [] and  height[cur] > height[stack[-1]]:
#                 h = height[stack[-1]]
#                 stack.pop()
#                 if stack == []:
#                     break
#             distance = cur - stack[-1] -1
#             min_ = min(height[cur],height(stack[-1]))
#             sum_ = sum_ + distance * (min_ - h)
#         stack.append(cur)
#         cur += 1
#         return sum_





