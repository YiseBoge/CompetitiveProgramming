class Solution:
    def minCostClimbingStairs(self, cost: list) -> int:
        distances = {}
        self.take_steps(cost, 0, distances)
        return min(distances[0], distances[1])

    def take_steps(self, costs, current, distances):
        if current in distances:
            return distances[current]
        if current == len(costs) - 1:
            distances[current] = costs[current]
            return costs[current]
        if current > len(costs) - 1:
            return 0

        result = 1000001
        for i in range(2):
            new = current + i + 1
            new_res = self.take_steps(costs, new, distances)
            result = min(result, new_res)

        result += costs[current]
        distances[current] = result
        return result


def solution(l1):
    s = Solution()
    return s.minCostClimbingStairs(l1)


def main():
    inp1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    print(solution(inp1))


if __name__ == '__main__':
    main()
