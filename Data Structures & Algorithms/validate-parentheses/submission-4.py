from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # stack here is gonna list, deque is better 
        if len(s) < 2:
            return False

        stack = deque()
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif (c == ')' or c == ']' or c == '}') and len(stack) == 0:
                return False
            elif (c == ')' and stack.pop() != '(') or (c == ']' and stack.pop() != '[') or (c == '}' and stack.pop() != '{'):
                return False 

        return len(stack) == 0
