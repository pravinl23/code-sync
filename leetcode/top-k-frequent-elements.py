class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        swap = [[] for i in range(len(nums) + 1)]
        for n in counter:
            swap[counter[n]].append(n)
            
        res = []
        for i in range(len(swap) - 1, 0, -1):
            if swap[i] != []:
                for num in swap[i]:
                    res.append(num)
            if len(res) == k:
                return res

        return res