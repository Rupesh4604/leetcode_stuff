class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # X and (X-1) = 0 if X is a power of 2 (set bit followed by zeroes; 
        # X= 10000... and X-1 = 01111...  )
        return n>0 and n&(n-1)==0