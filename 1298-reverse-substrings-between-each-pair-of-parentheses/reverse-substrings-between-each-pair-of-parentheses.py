from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ')':
                stack.append(char)
            else:
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # Remove the '('
                stack.extend(temp)  # Add the reversed substring back to stack
        
        return ''.join(stack)
                 
