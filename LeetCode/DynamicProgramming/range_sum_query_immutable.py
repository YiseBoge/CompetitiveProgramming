class NumArray:

    def __init__(self, nums: list):
        self.sums = [0]
        s = 0
        for i in nums:
            s += i
            self.sums.append(s)

    def sumRange(self, i: int, j: int) -> int:
        last = self.sums[j + 1]
        first = self.sums[i]
        return last - first


def solution(l1, l2, l3):
    s = NumArray(l1)
    return s.sumRange(l2, l3)


def main():
    inp = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    inp1 = 3
    inp2 = 5

    print(solution(inp, inp1, inp2))


if __name__ == '__main__':
    main()
