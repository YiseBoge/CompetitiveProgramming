class ProductOfNumbers:

    def __init__(self):
        self.products = []

    def add(self, num: int) -> None:
        if num == 0:
            self.products = []
        elif len(self.products) == 0:
            self.products.append(num)
        else:
            self.products.append(num * self.products[-1])

    def getProduct(self, k: int) -> int:
        if len(self.products) < k:
            return 0
        if len(self.products) == k:
            return self.products[-1]
        last_index = k + 1
        return self.products[-1] // self.products[-last_index]


def main():
    inp1 = [
        [0, 0, 2, 2],
        [1, 0, 2, 3],
        [1, 0, 3, 1]
    ]

    obj = ProductOfNumbers()
    obj.add(5)
    obj.add(0)
    obj.add(3)
    obj.add(4)
    print(obj.getProduct(2))


if __name__ == '__main__':
    main()
