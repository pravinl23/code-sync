class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        neg = 0
        if dividend < 0:
            neg += 1
        if divisor < 0:
            neg += 1
        if ((neg % 2) == 0):
            neg = 1
        else:
            neg = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        counter = 0
        while dividend >= 0:
            temp = divisor
            multiple = 1
            while temp*2 < dividend:
                temp *= 2
                multiple *= 2
            dividend -= temp
            counter += multiple
        
        return (counter - 1) * neg