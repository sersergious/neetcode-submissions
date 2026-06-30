class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Looked up the solution. Total time was 1hr 5 mins
        # Seem to understand it, it's all about using right and left
        # properly

        freq = {}
        left = 0
        longest = 0
        maxF = 0

        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            maxF = max(freq[s[right]], maxF)

            while (right - left + 1) - maxF > k:
                freq[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
            
        
        return longest
