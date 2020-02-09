class Solution:
    def minCostToMoveChips(self, chips: list) -> int:
        evens, odds = 0, 0
        for i in range(len(chips)):
            if chips[i] % 2 == 0:
                evens += 1
            else:
                odds += 1

        return min(evens, odds)


def solution(l1):
    s = Solution()
    return s.minCostToMoveChips(l1)


def main():
    inp1 = [2, 2, 2, 3, 3]

    print(solution(inp1))


if __name__ == '__main__':
    main()
