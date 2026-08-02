class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/":
                num1 = stack.pop()
                num2 = stack.pop()

                match(tokens[i]):
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num2 - num1)
                    case "*":
                        stack.append(num1 * num2)
                    case "/":
                        stack.append(int(float(num2) / num1))
            else:
                stack.append(int(tokens[i]))

        return stack.pop()        