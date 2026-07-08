class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff=0
        l=0
        for r in range(len(prices)):
            if prices[r]<prices[l]:
                l=r
            if maxdiff<prices[r]-prices[l]:
                maxdiff=prices[r]-prices[l]
        return maxdiff