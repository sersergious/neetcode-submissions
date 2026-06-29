class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solved using Solution bc stupid
        # Learned susbtring
        
        mp = {}
        l, res = 0, 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
        
        
        
                