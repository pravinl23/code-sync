class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
                left, right = 0,0
                if n-1 in d:
                    left = d[n-1]
                if n+1 in d:
                    right = d[n+1]
                d[n] += left + right
                d[n+right] = d[n]
                d[n-left] = d[n]
                
                if d[n] > max_len:
                    max_len = d[n]


        return max_len