class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = []
        t_letters = []
        
        for i in range(len(s)):
            s_letters.insert(i, s[i:i+1])

        for i in range(len(t)):
            t_letters.insert(i, t[i:i+1])
        
        s_letters.sort()
        t_letters.sort()

        return s_letters == t_letters
