class Solution:

    def isAnagram(self, str1: str, str2:str):
        if len(str1) != len(str2):
            return False

        s_letters = list(str1)
        t_letters = list(str2)
        
        s_letters.sort()
        t_letters.sort()
        
        return s_letters == t_letters


    def findAnagram(self, strs: List[str], strTarget: str):
        for s in strs:
            if (self.isAnagram(s, strTarget)): 
                return s
        
        return None

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMapped = {}

        for s in strs:
            potAnagram = self.findAnagram(strsMapped.keys(), s)
            if potAnagram is not None:
                strsMapped[potAnagram].append(s)
            else:
                strsMapped[s] = [s]

        result = []
        
        for anagrams in strsMapped.values():
            result.append(anagrams)

        return result