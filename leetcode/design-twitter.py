class Twitter:

    def __init__(self):
        self.time = 0  # global timestamp to order tweets
        self.followList = defaultdict(set)  # {userId: set(followingIds)}
        self.feed = defaultdict(list)  # {userId: [(time, tweetId), ...]}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        # append (negative time, tweetId) for max-heap sorting
        self.feed[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # include user's own last 10 tweets
        for tweet in self.feed[userId][-10:]:
            heapq.heappush(heap, tweet)

        # include each followee's last 10 tweets
        for followee in self.followList[userId]:
            for tweet in self.feed[followee][-10:]:
                heapq.heappush(heap, tweet)

        # take up to 10 most recent tweets overall
        most_recent = heapq.nsmallest(10, heap)
        most_recent.sort()  # sort back to most recent first
        return [tweetId for _, tweetId in most_recent]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followList:
            if followeeId in self.followList[followerId]:
                self.followList[followerId].remove(followeeId)