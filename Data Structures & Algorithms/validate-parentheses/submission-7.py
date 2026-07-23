class Solution:
    # This is just a warm up type of problem
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:

            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif (char == ')' or char == '}' or char == ']') and len(stack) == 0:
                return False
            elif char == ')' and stack.pop() != '(' or char == ']' and stack.pop() != '[' or char == '}' and stack.pop() != '{':
                return False
        
        return len(stack) == 0