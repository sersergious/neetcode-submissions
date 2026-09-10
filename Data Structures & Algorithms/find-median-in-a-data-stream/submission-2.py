class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and self.minHeap[0] < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1 * num)
        
        if len(self.maxHeap) + 1 < len(self.minHeap):
            n = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * n)
        elif len(self.minHeap) + 1 < len(self.maxHeap):
            n = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, n)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        elif len(self.minHeap) < len(self.maxHeap):
            return float(-1 * self.maxHeap[0])
        else:
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2.0
        