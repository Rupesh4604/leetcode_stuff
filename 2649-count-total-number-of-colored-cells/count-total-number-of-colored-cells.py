class Solution:
    def coloredCells(self, n: int) -> int:
        # if n==1:
        #     return 1
        # total = 1
        # for i in range(1,n):
        #     total += 4*i
        # return total
        return 1+2*n*(n-1)