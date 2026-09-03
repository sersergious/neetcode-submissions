
class Twitter:

    def __init__(self):
        self.time = 0
        self.usersMap = defaultdict(set)
        self.tweetsMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None: 
        self.tweetsMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        watching = self.usersMap[userId] | {userId}

        for user in watching:
            for t, tweet in self.tweetsMap[user]:
                heapq.heappush(minHeap, (t, tweet))
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        res = [] 
        
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        res.reverse()
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.usersMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usersMap[followerId].discard(followeeId)
