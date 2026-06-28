class Solution:
    
    def toAlnum(self, s: str) -> str:
        return ''.join(char for char in s if char.isalnum())
   
    def isPalindrome(self, s: str) -> bool:
        s = self.toAlnum(s)
        ptr1 = len(s) - 1
        ptr2 = 0

        while ptr2 < len(s) and ptr1 >= 0:
            print(s[ptr1])
            print(s[ptr2])

            char1 = s[ptr1].lower()
            char2 = s[ptr2].lower()

            if char1 != char2:
                return False
            
            ptr1 -= 1
            ptr2 += 1
        
        return True