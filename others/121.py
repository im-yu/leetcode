# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         ans = 0
#         for i in range(len(prices)-1):
#             for j in range(i+1,len(prices)):
#                 if ans < (prices[j]-prices[i]):
#                     ans = prices[j]-prices[i]
#         return ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last = 0
        ans = 0
        for i in range(len(prices)-1):
            last = max(0,(last + prices[i+1] - prices[i]))
            ans = max(ans,last)
        return ans