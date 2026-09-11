class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        
        while q or maxHeap:
            time += 1
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                task = q.popleft()
                heapq.heappush(maxHeap, task[0])
            
        return time
