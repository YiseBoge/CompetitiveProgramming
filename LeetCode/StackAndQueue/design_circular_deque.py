class MyCircularDeque:

    def __init__(self, k: int):
        self.list = [None] * k
        self.front = 0
        self.back = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.back = (self.back + 1) % len(self.list)
        else:
            self.front = (self.front - 1) % len(self.list)

        self.list[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.list[self.back] = value
        self.back = (self.back + 1) % len(self.list)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.list[self.front] = None
        self.front = (self.front + 1) % len(self.list)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.back = (self.back - 1) % len(self.list)
        self.list[self.back] = None

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.list[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.list[self.back - 1]

    def isEmpty(self) -> bool:
        return self.front == self.back and self.list[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.back and self.list[self.front] is not None


def main():
    # Your MyCircularDeque object will be instantiated and called as such:

    obj = MyCircularDeque(3)
    print(obj.insertFront(3))
    print(obj.insertLast(2))
    print(obj.insertLast(5))
    print(obj.deleteFront())
    print(obj.deleteLast())
    print(obj.getFront())
    print(obj.getRear())
    print(obj.isEmpty())
    print(obj.isFull())


if __name__ == '__main__':
    main()
