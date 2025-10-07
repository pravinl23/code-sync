class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums.sort()
        #for i in range(len(nums)):
        #    if nums[i] != i:
        #        return i
        #return len(nums)

        n = len(nums)
        expectedSum = n*(n+1)//2
        missing = expectedSum - sum(nums)

        return missing