class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def robHelper(lon):
            n = len(lon)
            dp = [0] * n
            dp[n - 1] = lon[n - 1]
            dp[n - 2] = max(lon[n-1], lon[n - 2])
            dp[n - 3] = max(lon[n - 3] + lon[n - 1], lon[n - 2])
            # skip the last 3
            for i in range(n - 4, -1, -1):
                dp[i] = max(dp[i + 2] + lon[i], dp[i + 1])
            return dp[0]

        l = len(nums)
        if l <= 3:
            return max(nums)
        list1 = nums[0:l - 1]
        list2 = nums[1:l]
        return max(robHelper(list1), robHelper(list2))