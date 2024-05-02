class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        points = sum(cardPoints[:k])
        n = len(cardPoints)
        points_temp = points
		
        for i in range(k):
            left_idx_to_substract = k - i - 1
            right_idx_to_add = n - i - 1
            points_temp -= cardPoints[left_idx_to_substract]
            points_temp += cardPoints[right_idx_to_add]
            points = max(points, points_temp)
        return points