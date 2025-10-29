class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        globalmax = 0
        localmax = 0
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if localmax + diff < 0:
                localmax = 0
            else:
                localmax += diff
                globalmax = max(localmax, globalmax)

        return globalmax