class Solution:
    # Time: 12
    # Reflection: second attempt - still did it brute force via sorting the array. There's gotta be an optimal solution via Max Heap that I learned but apparently did not recall. 

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            dist = -(x*x + y*y)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
            
        return res

    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     points.sort(key=lambda x: (x[0]**2 + x[1]**2))

    #     return points[0:k]

        



