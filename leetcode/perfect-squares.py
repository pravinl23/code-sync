class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n + 1)]
        
        iteration = 1
        while (iteration * iteration <= n):
            square = iteration * iteration
            for i in range(square, n + 1):
                # min of the next lowest square + 1 and itself
                dp[i] = min(dp[i - square] + 1, dp[i])
            iteration += 1
                

        return dp[n]