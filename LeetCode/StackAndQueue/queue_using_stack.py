class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        buffer = []
        while len(self.data) > 0:
            buffer.append(self.data.pop())

        x = buffer.pop()
        while len(buffer) > 0:
            self.data.append(buffer.pop())
        return x

    def peek(self) -> int:
        buffer = []
        while len(self.data) > 0:
            buffer.append(self.data.pop())

        x = buffer.pop()
        self.data.append(x)
        while len(buffer) > 0:
            self.data.append(buffer.pop())
        return x

    def empty(self) -> bool:
        return len(self.data) <= 0


def main():
    obj = MyQueue()
    obj.push(4)
    obj.push(5)
    print(obj.pop())
    print(obj.peek())
    print(obj.empty())


if __name__ == '__main__':
    main()
