# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return ([i,j])
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n=0
#         for i in range(len(nums)):
#             n+=1
#             if (target-nums[i]) in nums[i+1:]:
#                     return ([i,nums[i+1:].index(target - nums[i])+n])
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i,j in enumerate(nums):
#             if j in hashmap:
#                 return [hashmap.get(j),i]
#             hashmap[target - j] = i

#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for index,num in enumerate(nums):
#             another_num = target - num
#             if another_num in hashmap:
#                 return [hashmap[another_num],index]
#             hashmap[num] = index

