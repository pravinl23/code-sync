class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = []

        for i in range(len(prices) - 1):
            diff.append(prices[i + 1] - prices[i])
        globalmax = 0
        localmax = 0
        for i in range(len(diff)):
            if localmax + diff[i] < 0:
                localmax = 0
            else:
                localmax += diff[i]
                globalmax = max(localmax, globalmax)

        return globalmax