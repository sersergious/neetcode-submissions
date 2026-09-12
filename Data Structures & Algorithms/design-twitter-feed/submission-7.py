class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append([self.time, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:

        watching = self.users[userId] | {userId}
        minHeap = []

        for user in watching:
            tweets = self.tweets[user]
            
            for tweet in tweets:
                heapq.heappush(minHeap, tweet)

            while len(minHeap) > 10:
                    heapq.heappop(minHeap)
        res = []
        
        while minHeap:
            record = heapq.heappop(minHeap)
            res.append(record[1])
        
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
