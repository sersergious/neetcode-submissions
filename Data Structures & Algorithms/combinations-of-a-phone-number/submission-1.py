class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToChars = {"2": "abc",
                         "3": "def",
                         "4": "ghi",
                         "5": "jkl",
                         "6": "mno",
                         "7": "pqrs",
                         "8": "tuv",
                         "9": "wxyz"}
        res = []

        def dfs(cur, i):
            if i == len(digits):
                res.append("".join(cur))
                return
            
            chars = digitsToChars[digits[i]]

            for c in chars:
                cur.append(c)
                dfs(cur, i + 1)
                cur.pop()
        if digits:
            dfs([], 0)
        return res