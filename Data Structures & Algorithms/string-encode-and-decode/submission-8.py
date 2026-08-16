class Solution:

    def encode(self, strs: List[str]) -> str:
        masterStr = ""  

        for s in strs:
            masterStr += f'{len(s)}#{s}'
        
        print(masterStr)
        return masterStr

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        
        while j < len(s):
            while s[j] != "#":
                j += 1
    
            sLen = int(s[i:j])
            i = j + 1
            j = j + sLen +1
            res.append(s[i:j])
            i = j

        return res




