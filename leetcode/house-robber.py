class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = {}
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0] + nums[2], nums[1])

        dp[n - 1] = nums[n - 1]
        dp[n - 2] = nums[n - 2]
        dp[n - 3] = max(nums[n - 3] + nums[n - 1], nums[n - 2])
        
        for i in range(n - 4, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1], nums[i] + dp[i + 3])

        return dp[0]