class Solution:
    def sumZero(self, n: int) -> list:
        half = n // 2
        result = []
        for i in range(1, half + 1):
            result.append(i)
            result.append(-i)

        if n % 2 != 0:
            result.append(0)

        return result


def solution(l1):
    s = Solution()
    return s.sumZero(l1)


def main():
    inp1 = 10

    print(solution(inp1))


if __name__ == '__main__':
    main()
