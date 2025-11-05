#User function Template for python3

class Solution:
    def findMinSum(self, A,B,N):
        A.sort()
        B.sort()
        total = 0
        for i in range(N):
            total += abs(A[i]-B[i])
        return total