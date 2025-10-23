class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1


        coins.sort(reverse = True)

        # create a queue of all the calculations to make, not of coins
        # amount, count, (at 0 coins used we have full amount)
        start = (amount, 0)
        queue = deque([start])


        # amounts to avoid (if we checked 8 and it led to nothing, dont check again)
        seen = set()


        while queue:
            curr = queue.popleft()
            for c in coins:
                if curr[0] == 0:
                    return curr[1]
                elif curr[0] - c == 0:
                    return curr[1] + 1
                elif curr[0] - c > 0 and curr[0] - c not in seen:
                    seen.add(curr[0] - c)
                    queue.append([curr[0] - c, curr[1] + 1])

        return -1