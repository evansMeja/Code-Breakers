# Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.

# Return the qtt after dividing dividend by divisor.

# The integer division should truncate toward zero, which means losing its
# fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.



class Solution:
    MINUMUM_INTEGER = pow(-2, 31)
    MAXIMUM_INTEGER = pow(2, 31) - 1

    def recursiveDivide(self, currentDividend: int, currentDivisor: int):
        
        qtt = 1
        acc = currentDivisor  
        
        
        # normal case
        
        if currentDividend < currentDivisor:
            return 0
        elif currentDividend == currentDivisor:
            return 1

        while acc < currentDividend:
            qtt = qtt << 1
            acc = acc << 1  

        
        acc = acc >> 1
        qtt = qtt >> 1
        return qtt + self.recursiveDivide(currentDividend - acc, currentDivisor)

    def divide(self, dividend: int, divisor: int) -> int:
        
        ngt = False
        if (dividend >= 0 and divisor >= 0):
            ngt = False
        elif (dividend < 0 and divisor >= 0):
            ngt = True
        elif (dividend > 0 and divisor <= 0):
            ngt = True

        
        absDividend, absDivisor = abs(dividend), abs(divisor)

        
        if (absDivisor == 1):
            if (ngt == True):
                return -absDividend if Solution.MINUMUM_INTEGER < -absDividend else Solution.MINUMUM_INTEGER
            else:
                return absDividend if Solution.MAXIMUM_INTEGER > absDividend else Solution.MAXIMUM_INTEGER

        result = self.recursiveDivide(absDividend, absDivisor)
        return result if ngt == False else -result
