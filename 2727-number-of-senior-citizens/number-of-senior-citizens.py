class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 if int(a[11:13])>60 else 0 for a in details)
