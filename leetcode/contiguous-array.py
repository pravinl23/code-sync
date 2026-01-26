class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, zeroes = 0, 0
        prefix_diff = {0: -1} 

        res = 0

        for i, num in enumerate(nums):
            if num == 0:
                zeroes += 1
            else:
                ones += 1
            
            diff = ones - zeroes
            
            if diff in prefix_diff:
                res = max(res, i - prefix_diff[diff])
            else:
                prefix_diff[diff] = i


        return res