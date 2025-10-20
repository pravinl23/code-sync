class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        totalMoves = m-1 + n-1
        t = 1
        for i in range(1, totalMoves + 1):
            t *= i

        # (m - 1) !
        mFactorial = 1
        for i in range(1, m):
            mFactorial *= i
        
        # (n - 1)!
        nFactorial = 1
        for i in range(1, n):
            nFactorial *= i
        
        mFactorial *= nFactorial
        t /= mFactorial

        return t