class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # this is not optimal for space
        
        left, right = 0, len(s1) - 1

        print(right)
        while right < len(s2):
            print(s2[left:right+1])
            end = right + 1
            if self.isAnagram(s1, s2[left:end]):
                return True
            
            left += 1
            right += 1
        
        return False

    def isAnagram(self, s1, s2) -> bool:
        if(len(s1) != len(s2)):
            return False
        
        freq = {chr(i): 0 for i in range(97, 123)} # ascii
        
        for c in s1:
            freq[c] += 1
        
        for c in s2:
            freq[c] -= 1
            
        for key in freq.keys():
            if freq[key] != 0:
                return False 

        return True
