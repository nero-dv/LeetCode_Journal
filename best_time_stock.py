import enum


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        left_idx = 0
        
        for right_idx in range(1, len(prices)):
            if prices[right_idx] <= prices[left_idx]:
                left_idx = right_idx
            res = max(res, prices[right_idx]-prices[left_idx])
        return res

        
        
prices = [3, 3, 6, 3, 0]
print(Solution().maxProfit(prices))