class Solution:
    def divisorGame(self, N: int) -> bool:
        checked = {1: False}
        self.check_only(N, checked)
        return checked[N]

    def check_only(self, N, checked):
        if N in checked:
            return checked[N]

        result = False
        for x1 in range(N - 1, 0, -1):
            if N % x1 == 0:
                N2 = N - x1
                res = True
                for x2 in range(N2 - 1, 0, -1):
                    if N2 % x2 == 0:
                        N3 = N2 - x2
                        res = res and self.check_only(N3, checked)

                result = result or res

        checked[N] = result
        return result


def solution(l1):
    s = Solution()
    return s.divisorGame(l1)


def main():
    inp1 = 30

    print(solution(inp1))


if __name__ == '__main__':
    main()
