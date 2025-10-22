class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        def backtracking(n):
            if n in dp:
                return dp[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            res = 0 + backtracking(n - 2) + backtracking (n - 1)
            dp[n] = res
            return res

        return backtracking(n)