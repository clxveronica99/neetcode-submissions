class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        res = 0
        n = len(prices)
        for i in range(n):
            curr = prices[i]
            min_price = min(curr, min_price)
            res = max(res, curr-min_price)

        return res
                