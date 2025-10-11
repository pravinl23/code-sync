class Solution(object):
    dp = {}  # memoization cache
    
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        output = max(nums)

        currMax = 1
        currMin = 1

        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1
                continue
            tmp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            output = max(output, currMax)

        
        return output