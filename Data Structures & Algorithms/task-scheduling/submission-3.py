from _heapq import heappush
# Time: 20
# Reflection: this was one of those tougher problems. I had no chance of getting the brute force. Ironically, the optimal solution is easier to understand from the first glance. I only now need to study this untimed because I dont fully understand it yegt.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while q or maxHeap:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: 
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time 