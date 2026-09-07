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
                c = heapq.heappop(maxHeap)
                c += 1

                if c:
                    task = [c, time + n]
                    q.append(task)
            
            if q and time == q[0][1]:
                task = q.popleft()
                heapq.heappush(maxHeap, task[0])

        return time
