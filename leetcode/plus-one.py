class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        end = len(digits) - 1
        while digits[end] == 9:
            digits[end] = 0
            end -= 1
            
        if end < 0:
            digits.insert(0,1)
        else:
            digits[end] += 1
        
        return digits