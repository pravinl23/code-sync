class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 1:
            return
        onesCounter = 0
        read = 0
        write = 0

        # first only deal with 0's
        while read < len(nums):
            if nums[read] == 0:
                if nums[write] == 1:
                    onesCounter += 1
                nums[write] = 0
                write += 1
                read += 1
            else:
                read += 1

        # add 1's

        while onesCounter != 0:
            if nums[write] == 1:
                write += 1
            else:
                nums[write] = 1
                write += 1
                onesCounter -= 1
        
        read = write
        while read < len(nums):
            if nums[read] == 1:
                nums[write] = 1
                write += 1
                read += 1
            else:
                read += 1

        while write < len(nums):
            nums[write] = 2
            write += 1