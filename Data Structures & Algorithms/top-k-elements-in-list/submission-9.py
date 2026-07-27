class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        
        # Map num count
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(count)
        # Establish freq
        for key, val in count.items():
            freq[val].append(key)
        
        print(freq)
        # Count freq until k
        i = len(freq) - 1 
        while i >= 0:
           
            if freq[i] != []:
                j = 0
                while len(res) < k and j < len(freq[i]):
                    res.append(freq[i][j])
                    j += 1
            i -= 1

        return res