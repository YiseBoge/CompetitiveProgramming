import math
import sys


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        r = math.floor(math.sqrt(num))
        total = 0
        for i in range(2, r + 1):
            if num % i == 0:
                total += (i + num // i)

        return total == num - 1


def solution(inp):
    s = Solution()
    return s.checkPerfectNumber(inp)


def main():
    in1 = 100
    sys.stdout.write(str(solution(in1)))


if __name__ == '__main__':
    main()
