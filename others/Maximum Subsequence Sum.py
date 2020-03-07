# K = 10
# nums = [-10,1,2,3,4,-5,-23,3,7,-21]
#
#
# n = K
# ans_sum = -1
# ans_right = n-1
# ans_left = 0
# tmp_sum = 0
# tmp_left = 0
# for i in range(1, n):
#     tmp_sum += nums[i]
#     if tmp_sum < 0:
#         tmp_sum = 0
#         tmp_left = i+1
#     elif tmp_sum > ans_sum:
#         ans_sum = tmp_sum
#         ans_right = i
#         ans_left = tmp_left
# print("%d %d %d"%(ans_sum,ans_left,ans_right))




#         curr_sum = max(nums[i], curr_sum + nums[i])
#         max_sum = max(max_sum, curr_sum)
#
#     return max_sum
# print(maxSubArray(nums))

# K = int(input())
# line = input()
# nums = list(map(int, line.split()))
#
# def maxSubArray(nums):
#     n = K
#     curr_sum = max_sum = nums[0]
#     for i in range(1, n):
#         curr_sum = max(nums[i], curr_sum + nums[i])
#         max_sum = max(max_sum, curr_sum)
#     return max_sum
# print(maxSubArray(nums))

K = int(input())
line = input()
nums = list(map(int, line.split()))

ans_sum = -1
ans_right = K-1
ans_left = 0
tmp_sum = 0
tmp_left = 0
for i in range(K):
    tmp_sum += nums[i]
    if tmp_sum < 0:
        tmp_sum = 0
        tmp_left = i+1
    elif tmp_sum > ans_sum:
        ans_sum = tmp_sum
        ans_right = i
        ans_left = tmp_left
if ans_sum < 0:ans_sum = 0
print("%d %d %d" % (ans_sum, nums[ans_left], nums[ans_right]))




