class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []
        numsSet = set(nums)
        numsNonDuplicate = list(numsSet)
        
        for i in numsNonDuplicate:
            count.update({i: 0})
        
        for num in nums:
            if num in count.keys():
                count[num] += 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res  