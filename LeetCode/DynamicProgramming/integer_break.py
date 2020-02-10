import math


class Solution:
    def integerBreak(self, n: int) -> int:
        found = {1: 1}

        for i in range(2, n + 1):
            temp = 0
            for j in range(1, math.ceil(i / 2) + 1):
                max1, max2 = max(j, found[j]), max(i - j, found[i - j])
                temp = max(temp, max1 * max2)
            found[i] = temp

        return found[n]


def solution(l1):
    s = Solution()
    return s.integerBreak(l1)


def main():
    inp1 = 54

    print(solution(inp1))


if __name__ == '__main__':
    main()
