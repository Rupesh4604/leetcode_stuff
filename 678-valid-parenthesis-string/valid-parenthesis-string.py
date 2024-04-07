class Solution:
    def checkValidString(self, s: str) -> bool:
        open_par = []
        spl_char = []
        for i,char in enumerate(s):
            if char=='(':
                open_par.append(i)
            elif char =='*':
                spl_char.append(i)
            else:
                if open_par:
                    open_par.pop()
                elif spl_char:
                    spl_char.pop()
                else:
                    return False
        
        # Dealing with unbalanced parenthesis 
        while open_par and spl_char:
            if open_par[-1] < spl_char[-1]:
                open_par.pop()
                spl_char.pop()
            else:
                break
        return not open_par

        