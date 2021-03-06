class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        currMin = self.getMin()
        if currMin == None or x < currMin:
            currMin = x
        self.stack.append((x, currMin))


    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return None
        del self.stack[-1]


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
