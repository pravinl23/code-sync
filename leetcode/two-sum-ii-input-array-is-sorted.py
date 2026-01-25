class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        while l < len(numbers):
            r = l + 1
            while r < len(numbers) - 1 and numbers[l] == numbers[r + 1]:
                l += 1
                r += 1
            while r < len(numbers):
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                if numbers[l] + numbers[r] > target:
                    break
                r += 1


            l += 1