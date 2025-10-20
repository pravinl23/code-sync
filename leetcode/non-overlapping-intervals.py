class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if not intervals:
            return 0
        #sorts it in order of end time (increasing order)
        # e.g [3,4][5,8][1,2] -> [1,2][3,4][5,8] (2,4,8)
        # we do this because hypothetically lets say we had an interval that was really long
        # like 100 terms, [1,100] this means if its sorted in order every single smaller interval would 
        # come first so [1,2][3,6][10,30] etc ect, thus maximizing the total we choose
        intervals.sort(key=lambda x: x[1])        
        remove = 0
        currLatest = intervals[0][1]
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] < currLatest:   
                remove += 1
            else:
                currLatest = intervals[i][1]

        return remove