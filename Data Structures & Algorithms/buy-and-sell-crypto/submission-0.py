class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res,l = 0,0
        for r in range(len(prices)):

            if prices[l]>prices[r]:
                while prices[l]>prices[r]:
                    l+=1
            res = max(res,prices[r]-prices[l])
        return res