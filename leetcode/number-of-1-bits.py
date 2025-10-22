class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        divider = 1
        for i in range(1, 31):
            divider *= 2
        counter = 0
        while n != 0:
            if n >= divider:
                counter += 1
                n -= divider
            divider /= 2

        return counter