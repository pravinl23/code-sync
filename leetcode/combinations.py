class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def backtracking(path, i):            
            if len(path) == k:
                res.append(path[:])
                return
            if i > n:
                return

            # case 1 include
            path.append(i)
            backtracking(path, i + 1)
            path.pop()

            # case 2 exclude
            backtracking(path, i + 1)


        backtracking([], 1)
        return res