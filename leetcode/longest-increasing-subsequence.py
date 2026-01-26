class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        tail = []

        for n in nums:
            if not tail:
                tail.append(n)
            else:
                insert = bisect_left(tail, n)
                if insert == len(tail):
                    tail.append(n)
                else:
                    tail[insert] = n
        return len(tail)