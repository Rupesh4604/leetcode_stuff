class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minElem = prices[0]
        diff = 0

        for i in range(1,len(prices)):
            if prices[i]<minElem:
                minElem = prices[i]
            diff = max(diff, prices[i]-minElem)
        return diff

