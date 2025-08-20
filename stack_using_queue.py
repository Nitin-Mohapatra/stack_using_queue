class Queue:
    # Making a queue
    def __init__(self):
        self.data = []

    # enqueue
    def enqueue(self, ele):
        self.data.append(ele)

    # dequeue
    def dequeue(self):
        if len(self.data) != 0:
            return self.data.pop(0)
        else:
            return None

    # Front peek
    def frontPeek(self):
        if len(self.data) != 0:
            return self.data[0]
        else:
            return None

    # isEmpty
    def is_Empty(self):
        return len(self.data) == 0


class MyStack(object):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # step 1. Add element to q2
        self.q2.enqueue(x)

        # step 2. Move all elements from q1 to q2
        while not self.q1.is_Empty():
            self.q2.enqueue(self.q1.dequeue())

        # step 3. Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.dequeue()

    def top(self):
        """
        :rtype: int
        """
        return self.q1.frontPeek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.q1.is_Empty()


# Example usage:
obj = MyStack()
obj.push(10)
obj.push(20)
print(obj.top())    # 20
print(obj.pop())    # 20
print(obj.empty())  # False
print(obj.pop())    # 10
print(obj.empty())  # True
