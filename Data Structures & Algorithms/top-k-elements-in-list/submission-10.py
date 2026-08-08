class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time 
        # Reflection

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        # to map elements and their counts
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for key in count.keys():
            freq[count[key]].append(key)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            if len(freq[i]) == 0:
                continue

            l = freq[i]
            for s in freq[i]:
                if len(res) != k:
                    res.append(s)
                else:
                    return res
            
        return res
                
            

