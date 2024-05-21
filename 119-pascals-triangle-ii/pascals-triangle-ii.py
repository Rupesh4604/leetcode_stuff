class Solution:
    @staticmethod
    def ncr(n,r):
        res = 1
        for i in range(r):
            res = res*(n-i)
            res = res//(i+1)
        return int(res)

    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        row =rowIndex+1
        for col in range(1,row+1):
            ans.append(self.ncr(row-1,col-1))
        return ans