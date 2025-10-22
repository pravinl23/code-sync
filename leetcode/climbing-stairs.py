class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # O(n) space complexity - recursive
        '''
        dp = {}
        def backtracking(n):
            if n in dp:
                return dp[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            dp[n] = backtracking(n - 2) + backtracking(n - 1)
            return dp[n]

        return backtracking(n)
        '''

        # O(1) space complexity - iterative (just fibonnaci)
        if n <= 2:
            return n
        n1 = 1
        n2 = 2
        for _ in range(3, n + 1):
            n1, n2 = n2, n1 + n2
        return n2