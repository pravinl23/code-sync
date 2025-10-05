from collections import defaultdict

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
                if (n+1 in d) and (n-1 in d):
                    d[n] = d[n+1] + d[n-1] + d[n]
                    d[n+d[n+1]] = d[n]
                    d[n-d[n-1]] = d[n]
                elif n+1 in d:
                    d[n] = d[n+1] + d[n]
                    d[n+d[n+1]] = d[n]
                elif n-1 in d:
                    d[n] = d[n-1] + d[n]
                    d[n-d[n-1]] = d[n]

                if d[n] > max:
                    max = d[n]


        return max