class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices.insert(0,10000)
        dp = [0 for i in range(len(prices))]
        if len(prices) == 1:
            return 0
       
        pivot = prices[len(prices) - 1]
        runningSum = 0
        for i in range(len(prices) - 2, -1, -1):

            delta = prices[i + 1] - prices[i]
            localSum = pivot - prices[i]
            if delta < 0:
                dp[i] = max(runningSum, localSum)
                pivot = prices[i]
                runningSum = 0
            else:
                runningSum = max(localSum, runningSum)

        return sum(dp)