class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min=0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min=x
        else:
            self.stack.append(x-self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        a=self.stack.pop()
        if  a<0:
            self.min = self.min - a

    def top(self):
        """
        :rtype: int
        """
        b=self.stack[-1]
        if b >0:
            return b+self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()