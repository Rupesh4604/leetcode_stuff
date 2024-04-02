import math 

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge case where divisor is 0 or when dividend is 0
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        if dividend == 0:
            return 0
        
        # Handle overflow cases
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
            
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Convert both dividend and divisor to positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        # Initialize quotient and temp variables
        quotient = 0
        temp = 0
        
        # Iterate through bits of dividend from left to right
        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                quotient |= 1 << i
        
        # Adjust sign of quotient
        if negative:
            quotient = -quotient
        
        return quotient
