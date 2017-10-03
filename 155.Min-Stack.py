class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        self.min_queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        if len(self.min_queue) == 0 or self.min_queue[-1] >= x:
            self.min_queue.append(x)

    def pop(self):
        """
        :rtype: void
        """
        x = self.queue.pop()
        if len(self.min_queue) != 0 and self.min_queue[-1] == x:
            self.min_queue.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.queue) == 0:
            return []
        return self.queue[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_queue) == 0:
            return []
        return self.min_queue[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
