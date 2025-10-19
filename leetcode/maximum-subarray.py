class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        global_max = nums[0]
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr > global_max:
                global_max = curr
            if curr < 0:
                curr = 0

        return global_max