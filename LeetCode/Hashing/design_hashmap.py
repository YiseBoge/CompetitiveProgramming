class MyHashMap:

    def __init__(self):
        self.size = 1000003
        self.values = [None] * self.size

    def __str__(self):
        items = []
        for i in range(self.size):
            val = self.values[i]
            if val:
                st = str(i) + ": " + str(val)
                items.append(st)
        return str(items)

    def put(self, key: int, value: int) -> None:
        self.values[key] = value

    def get(self, key: int) -> int:
        v = self.values[key]
        return v if v is not None else -1

    def remove(self, key: int) -> None:
        self.values[key] = None


def main():
    obj = MyHashMap()
    obj.put(3, 5)
    print(obj)

    print(obj.get(3))

    obj.remove(3)
    print(obj)


if __name__ == '__main__':
    main()
