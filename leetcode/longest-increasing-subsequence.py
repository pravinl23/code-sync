class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = []
        for n in nums:
            longest.append(1)


        [1,2,3,4]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    longest[i] = max(longest[i], 1 + longest[j])
        return max(longest)