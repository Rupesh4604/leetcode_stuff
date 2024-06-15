class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n==1:
            return True
        
        def two(num):
            while num > 1:
                if num % 2 != 0:
                    return False
                num //= 2
            return True
        
        return two(n)