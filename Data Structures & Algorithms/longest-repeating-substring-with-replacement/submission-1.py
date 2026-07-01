class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Second attempt at the problem

        # grow window as long as its len - maxFreqLetter < k
        # if violated, shrink the window until match the condition
        # start: maxF = 0 but we update with max(maxF, freq[s[r]])
        # when shinking, don't forget to reduce freq[s[l]]
        freq = {}
        l = 0
        maxF = 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxF = max(maxF, freq[s[r]])

            while (r - l + 1) - maxF > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
    

            
