class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for s in details:
            if int(s[-4:-2])>60:
                count +=1
        return count