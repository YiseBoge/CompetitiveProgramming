class MyStack:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        for i in range(len(self.data) - 1):
            self.data.append(self.data.pop(0))
        x = self.data.pop(0)
        return x

    def top(self) -> int:
        for i in range(len(self.data) - 1):
            self.data.append(self.data.pop(0))
        x = self.data.pop(0)
        self.data.append(x)
        return x

    def empty(self) -> bool:
        return len(self.data) <= 0


def main():
    obj = MyStack()
    obj.push(4)
    obj.push(5)
    print(obj.pop())
    print(obj.top())
    print(obj.empty())


if __name__ == '__main__':
    main()
