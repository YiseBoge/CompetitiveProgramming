import sys


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        i = 1
        while 5 ** i <= n:
            counts = n // (5 ** i)
            result += counts
            i += 1

        return result


def solution(inp):
    s = Solution()
    return s.trailingZeroes(inp)


def main():
    in1 = 100
    sys.stdout.write(str(solution(in1)))


if __name__ == '__main__':
    main()
