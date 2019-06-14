# day 35 2019-06-13 Thu
# 155. Min Stack

class MinStack:
    # l = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> None:
        if self.l is None:
            return []
        else:
            self.l.pop()

    def top(self) -> int:
        if self.l:
            return self.l[-1]
        else:
            return []
    def getMin(self) -> int:
        if self.l:
            min = self.l[0]
            for i in self.l:
                if i < min:
                    min = i
            return min
        else:
            return []
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()