class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 2 pointer approach, read pointer and write pointer, write overwriters, read 
        # is always head, write moves as it updates elements in the list

        write = 2
        c = 2
        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
                c += 1

        return c