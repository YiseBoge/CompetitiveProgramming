class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min is None or x < self.min:
            self.min = x

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()

        self.min = min(self.stack) if len(self.stack) > 0 else None

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) > 0 else None

    def getMin(self) -> int:
        return self.min


def main():
    obj = MinStack()
    obj.push(4)
    obj.push(5)
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())


if __name__ == '__main__':
    main()
