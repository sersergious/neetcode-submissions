class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the window size could be num of cons sim chars + k
        # store update the longest substr 
        # readjust l ptr as long as size > k + freq of chars 

        freq = {}
        l = longest = 0
        maxF = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxF = max(maxF, freq[s[r]])

            while (r - l + 1) - maxF > k:
                freq[s[l]] -= 1
                l += 1

            longest = max(longest, r-l+1)    
        
        return longest
