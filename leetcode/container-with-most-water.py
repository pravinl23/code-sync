class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        maxS = 0
        while left < right:
            x = right - left
            y = min(height[left], height[right])

            if x*y > maxS:
                maxS = x * y
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxS