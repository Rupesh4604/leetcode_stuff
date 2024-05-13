class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        purchase = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]<purchase:
                purchase = prices[i] 
            profit = max(profit,prices[i]-purchase)
        return profit
