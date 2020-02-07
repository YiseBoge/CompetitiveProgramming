class Solution:
    def twoCitySchedCost(self, costs: list) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        result = 0

        half = len(costs) // 2
        for i in range(0, half):
            result += costs[i][0]

        for i in range(half, len(costs)):
            result += costs[i][1]

        return result


def solution(l1):
    s = Solution()
    return s.twoCitySchedCost(l1)


def main():
    inp1 = [[1000, 20], [30, 20], [400, 50], [30, 20], [1, 1], [30, 20]]

    print(solution(inp1))


if __name__ == '__main__':
    main()
