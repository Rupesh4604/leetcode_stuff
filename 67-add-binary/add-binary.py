class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        A simple answer using int function int(a,2) where 2 represents the base
        str(bin(int(a,2)+int(b,2)))[2:]
        '''
        carry = 0
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        res = ''
        for i in range(max_len-1,-1,-1):
            n1 = int(a[i])
            n2 = int(b[i])

            sum_digits = carry + n1 + n2
            carry = sum_digits//2
            res = str(sum_digits % 2) + res
        
        if carry:
            res = "1"+ res
        
        return res
