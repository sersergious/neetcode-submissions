class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)

            if s2 > s1:
                heapq.heappush(maxHeap, s1 - s2)
            elif s1 > s2:
                heapq.heappush(maxHeap, s2 - s1)
        
        maxHeap.append(0)
        return abs(maxHeap[0])


        
