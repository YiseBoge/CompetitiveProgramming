import sys


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        ans = set()
        for i in range(20):
            for j in range(20):
                temp = (x ** i) + (y ** j)
                if temp <= bound:
                    ans.add(temp)
        return list(ans)


def solution(l1, l2, l3):
    s = Solution()
    return s.powerfulIntegers(l1, l2, l3)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()

    inp1 = 2
    inp2 = 3
    inp3 = 10
    sys.stdout.write(str(solution(inp1, inp2, inp3)))


if __name__ == '__main__':
    main()
