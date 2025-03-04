import math 

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            x = n%3
            if x==2:
                return False
            n = n//3
        return True
        