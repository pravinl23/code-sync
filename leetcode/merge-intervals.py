class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[0])

        n = len(intervals)
        currLatestInterval = intervals[0]

        res = []
        for i in range(1, n):
            if intervals[i][0] <= currLatestInterval[1]:
                currLatestInterval = [min(intervals[i][0], currLatestInterval[0]), max(currLatestInterval[1], intervals[i][1])]
            else:
                res.append(currLatestInterval)
                currLatestInterval = intervals[i]

        res.append(currLatestInterval)

        return res