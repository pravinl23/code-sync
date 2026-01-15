class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                # go left
                left, right = mid, mid
                tempmid = mid
                while tempmid > 0:
                    tempmid -= 1
                    if nums[tempmid] == target:
                        left = tempmid
                # go right
                while tempmid < len(nums) - 1:
                    tempmid += 1
                    if nums[tempmid] == target:
                        right = tempmid

                return [left,right]

            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return [-1, -1]