class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        buckets = []
        seen = {}
        counter = 0
        for s in strs:
            inOrder = []
            for char in s:
                inOrder.append(char)
            inOrder.sort()
            inOrder = tuple(inOrder)

            if inOrder in seen:
                buckets[seen[inOrder]].append(s)
            else:
                seen[inOrder] = counter
                buckets.append([])
                buckets[counter].append(s)
                counter += 1
        

        return buckets