# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         a = list()
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         a.append({nums[i],nums[j],nums[k]})
#         return a

#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         a = []
#         hashmap = {}
#         target = []
#         for i in nums:
#             target = -nums
#         for target in target:
#             for index,num in enumerate(nums):
#                 another_num = target - num
#             if another_num in hashmap:
#                 a.append([hashmap.[another_num],index])
#             hashmap[num]=index
#         return a

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)-2):
            if nums[k] > 0: break
            if k >0 and nums[k] == nums[k-1]:
                continue
            i,j = k+1,len(nums)-1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                elif s > 0:
                    j -= 1
                else:
                    res.append((nums[k],nums[i],nums[j]))
                    while i < j and nums[i]==nums[i+1]:
                        i += 1
                    while i < j and nums[j]==nums[j-1]:
                        j -= 1
                    i += 1;j -= 1
        return res


