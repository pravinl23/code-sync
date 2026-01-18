class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums_set = set(nums)

        globalMax = 1
        for i in range(len(nums)):
            localMax = 0
            next = nums[i]
            prev = nums[i] - 1
            while next in nums_set:
                localMax += 1
                nums_set.remove(next)
                next += 1
            while prev in nums_set:
                localMax += 1
                nums_set.remove(prev)
                prev -= 1
            globalMax = max(localMax, globalMax)

        return globalMax