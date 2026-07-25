class Solution:
    def isAnagram(self, s1, s2):
        if len(s1) !=  len(s2):
            return False
        
        freq = [0] * 26
        
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
            freq[ord(s2[i]) - ord('a')] -= 1

        for i in range(len(freq)):
            if freq[i] != 0:
                return False
        
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hM = {}

        for s in strs:
            flag = False
            for key in hM.keys():
                if self.isAnagram(s, key):
                    hM[key].append(s)
                    flag = True
                    break
            
            if not flag:
                hM[s] = [s]
            
        res = []
        
        for vals in hM.values():
            res.append(vals)

        return res 