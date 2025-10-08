class Solution(object):
    def threeSum(self, nums):
        # target = 0
        d = {}
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            d = {}
            for j in range(i + 1, len(nums)):
                if nums[j] in d:
                    triplet = [nums[i], nums[d[nums[j]]], nums[j]]
                    if triplet not in res:
                        res.append(triplet)
                seek = target - nums[j]
                d[seek] = j

        return res