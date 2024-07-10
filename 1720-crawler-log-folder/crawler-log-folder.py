class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for log in logs:
            if log=='../':
                if counter:
                    counter -=1
            elif log=='./':
                continue
            else:
                counter += 1
        return counter

