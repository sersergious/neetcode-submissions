class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hM = {}
        longest = 0
        maxFreq = 0
        l = 0

        for r in range(len(s)):
            
            hM[s[r]] = 1 + hM.get(s[r], 0)
            maxFreq = max(maxFreq, hM[s[r]])

            while l < r and (r - l + 1) - maxFreq > k:
                hM[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)    
            
        return longest
