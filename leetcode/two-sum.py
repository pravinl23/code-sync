class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seek = {}
        for i in range(len(nums)):
            if nums[i] in seek:
                return [i, seek[nums[i]]]
            t = target - nums[i]
            seek[t] = i