class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time<n:
            return time+1
        else:
            cycles = time//(n-1)
            steps = time%(n-1)
            if cycles%2==0:
                return steps+1
            else:
                return n-steps