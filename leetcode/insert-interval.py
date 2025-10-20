class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        n = len(intervals)
        res = []
        insert = False
        for i in range(n):
            if newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
                newInterval = [min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])]
            elif newInterval[0] < intervals[i][0] and newInterval[1] < intervals[i][1]:
                res.append(newInterval)
                for itvl in intervals[i:]:
                    res.append(itvl)
                return res
            else:
                res.append(intervals[i])
        if not insert:
            res.append(newInterval)
        return res