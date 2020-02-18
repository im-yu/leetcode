# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         for i in nums[:]:
#             if i==0:
#                 nums.append(0)
#                 nums.remove(0)
#
# class Solution:
#      def moveZeroes(self, nums: List[int]) -> None:
#          j=0
#          for i in range(len(nums)):
#              if nums[i]:
#                  nums[j]=nums[i]
#                  j+=1
#          for i in range(j,len(nums)):
#                 nums[i]=0

class Solution:
     def moveZeroes(self, nums: List[int]) -> None:
         j=0
         for i in range(len(nums)):
             if nums[i]:
                 nums[j],nums[i]=nums[i],nums[j]
                 j+=1