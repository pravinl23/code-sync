class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = k - 1
        
        globalMin = None
        while r < len(nums):
            localMin = nums[r] - nums[l]
            if not globalMin:
                globalMin = localMin
            else:
                globalMin = min(globalMin, localMin)
            r += 1
            l += 1

        return globalMin