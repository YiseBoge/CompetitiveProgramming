import sys

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
"""


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x * y


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int):
        maximum = 1000
        results = []

        for i in range(1, maximum + 1):
            x = i
            y = self.findSoulMate(customfunction, z, x, 1, maximum)
            # print(y)
            if y is not None:
                results.append([x, y])

        return results

    def findSoulMate(self, customfunction, z, x, start, finish):
        middle = (finish + start) // 2
        val = customfunction.f(x, middle)

        if finish < start:
            return None
        if val > z:
            return self.findSoulMate(customfunction, z, x, start, middle - 1)
        if val < z:
            return self.findSoulMate(customfunction, z, x, middle + 1, finish)

        return middle


def solution(l1):
    s = Solution()
    c = CustomFunction()
    return s.findSolution(c, l1)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()

    inp1 = 10
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
