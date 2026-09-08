class Twitter:

    def __init__(self):
        self.time = 0
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        watching = self.users[userId] | {userId}
        newsFeed = []
        
        for user in watching:
            for tweet in self.tweets[user]:
                heapq.heappush(newsFeed, tweet)

                if len(newsFeed) > 10:
                    heapq.heappop(newsFeed)
                
        res = []
        
        while newsFeed:
            res.append(heapq.heappop(newsFeed)[1])
        
        res.reverse()
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
