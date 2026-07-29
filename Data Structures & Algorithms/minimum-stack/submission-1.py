class MinStack:

    def __init__(self):
        self.stack = []  

    def push(self, val: int) -> None:
        if self.stack:
            minCur = min(self.stack[-1][1], val)
            self.stack.append([val, minCur])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        record = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] 

    def getMin(self) -> int:
        return self.stack[-1][1]
