class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        coins.sort(reverse = True)
        queue = deque([[amount, 0]])
        seen = set()

        while queue:
            curr = queue.popleft()
            for c in coins:
                if curr[0] == 0:
                    return curr[1]
                if curr[0] - c >= 0 and curr[0] - c not in seen:
                    seen.add(curr[0] - c)
                    queue.append([curr[0] - c, curr[1] + 1])
        
        return -1