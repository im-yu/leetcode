class MyCircularDeque:

    def __init__(self, k: int):
        self.q = collections.deque(maxlen = k)

    def insertFront(self, value: int) -> bool:
        if len(self.q) < self.q.maxlen:
            self.q.appendleft(value)
            return True
        else:
            return False
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
    def insertLast(self, value: int) -> bool:
        if len(self.q) < self.q.maxlen:
            self.q.append(value)
            return True
        else:
            return False
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
    def deleteFront(self) -> bool:
        if self.q:
            self.q.popleft()
            return True
        else:
            return False
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
    def deleteLast(self) -> bool:
        if self.q:
            self.q.pop()
            return True
        else:
            return False
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
    def getFront(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1
        """
        Get the front item from the deque.
        """
    def getRear(self) -> int:
        if self.q:
            return self.q[-1]
        else:
            return -1
        """
        Get the last item from the deque.
        """
    def isEmpty(self) -> bool:
        return not self.q
        """
        Checks whether the circular deque is empty or not.
        """
    def isFull(self) -> bool:
        return len(self.q) == self.q.maxlen
        """
        Checks whether the circular deque is full or not.
        """