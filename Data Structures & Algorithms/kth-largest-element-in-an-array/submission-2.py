class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a min heap
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]