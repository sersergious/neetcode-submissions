class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/": 
                stack.append(int(token))
            else:
                tok1 = stack.pop()
                tok2 = stack.pop()
                match token:
                    case '+':
                        tokRes = tok1 + tok2
                    case '-':
                        tokRes = tok2 - tok1
                    case '/':
                        tokRes = int(float(tok2) / tok1)
                    case '*':
                        tokRes = tok1 * tok2

                stack.append(tokRes)
        
     

        return stack.pop()