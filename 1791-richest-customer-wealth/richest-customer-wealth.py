class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sums_list = [sum(sublist) for sublist in accounts]
        return max(sums_list)
            
        