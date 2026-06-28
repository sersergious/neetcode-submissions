class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""

        for st in strs:
            strLen = len(st)
            encodedStr += str(strLen) + '#' + st

        return encodedStr


    def decode(self, s: str) -> List[str]:
        print(s)
        
        decodedStrs = []
        
        j = 0

        while j < len(s):
            strLen = ""
            while s[j] != '#':
                strLen += s[j]
                j += 1

            j += int(strLen)
            start = j - int(strLen) + 1
            decodedStrs.append(s[start:j+1])
            
            j+= 1

        return decodedStrs

        