class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        res = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                break
            middle = (left + right) // 2
            res = min(nums[middle], res)

            # means its on the bigger half
            # [3, 4, 5, 1, 2], since 5 > 3, its on bigger half (left side)
            if nums[middle] >= nums[left]: 
                # this means its on the right side (smaller half)
                left = middle + 1
                # [3, 4, 5, 1, 2]
                #.       L  M  R
            else:
                right = middle - 1
        
        
        return res