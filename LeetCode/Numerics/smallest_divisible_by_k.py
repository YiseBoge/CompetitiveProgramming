import sys


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        result = 1
        n = 1

        while True:
            if result > K:
                return -1

            rem = n % K
            if rem == 0:
                return result

            n = (rem * 10) + 1;
            # n = n + 10 ** result
            result += 1


def solution(inp):
    s = Solution()
    return s.smallestRepunitDivByK(inp)


def main():
    in1 = 11
    sys.stdout.write(str(solution(in1)))


if __name__ == '__main__':
    main()
