class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {0: 1, 1: 1, 2: 2}
        self.count_ways(n, ways)
        return ways[n]

    def count_ways(self, n, ways):
        if n in ways:
            return ways[n]

        result = self.count_ways(n - 1, ways) + self.count_ways(n - 2, ways)
        ways[n] = result
        return result


def solution(l1):
    s = Solution()
    return s.climbStairs(l1)


def main():
    inp1 = 30

    print(solution(inp1))


if __name__ == '__main__':
    main()
