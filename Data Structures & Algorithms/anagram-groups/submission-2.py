class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time 
        # reflection

        hM = defaultdict(list)

        for s in strs:
            freq = [0] * 26

            for c in s:
                freq[ord(c) - ord('a')] += 1
            
            hM[str(freq)].append(s)
        res = []
        
        for val in hM.values():
            res.append(val)

        return res