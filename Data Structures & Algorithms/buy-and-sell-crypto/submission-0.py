class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy = prices[0]
        for sell in prices:
            prof = max(prof,sell-buy)
            buy = min(buy,sell)
        return prof