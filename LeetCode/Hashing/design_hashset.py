class MyHashSet:

    def __init__(self):
        self.size = 30011
        self.set = [None] * self.size

    def __str__(self):
        items = []
        for i in self.set:
            if i is None:
                i = []
            if len(i) == 0:
                continue
            items += i
        return str(items)

    def add(self, key: int) -> None:
        ind = self.make_hash(key)
        lst = self.set[ind]
        if lst is None:
            lst = []
        if key not in lst:
            lst.append(key)
        self.set[ind] = lst

    def remove(self, key: int) -> None:
        ind = self.make_hash(key)
        lst = self.set[ind]
        if lst is None:
            lst = []
        if key in lst:
            lst.remove(key)

    def contains(self, key: int) -> bool:
        ind = self.make_hash(key)
        lst = self.set[ind]
        if lst is None:
            lst = []
        return key in lst

    def make_hash(self, val) -> int:
        return val % self.size


def main():
    obj = MyHashSet()

    obj.add(5)
    obj.add(4)
    print(obj)

    obj.remove(5)
    print(obj)

    print(obj.contains(5))


if __name__ == '__main__':
    main()
