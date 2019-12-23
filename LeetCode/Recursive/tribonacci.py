import sys


class Solution:
    def tribonacci(self, n: int) -> int:
        ls = [0, 1, 1, 2]

        if n < 3:
            return ls[n]

        for i in range(3, n + 1):
            l0 = ls[0]
            l1 = ls[1]
            l2 = ls[2]
            l3 = l0 + l1 + l2

            ls = [l1, l2, l3, l3]

        return ls[-1]


def solution(inp):
    s = Solution()
    return s.tribonacci(inp)


def main():
    in1 = 37
    sys.stdout.write(str(solution(int(in1))))


if __name__ == '__main__':
    main()
