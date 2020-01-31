class Solution:
    def maxProfit(self, prices: list) -> int:
        profit = 0
        stock = 0
        selling = False

        for i in range(len(prices)):
            if selling and (i == len(prices) - 1 or prices[i] > prices[i + 1]):
                profit += prices[i] - stock
                stock = prices[i]
                selling = False
            elif not selling and (i == len(prices) - 1 or prices[i] < prices[i + 1]):
                stock = prices[i]
                selling = True

        return profit


def solution(l1):
    s = Solution()
    return s.maxProfit(l1)


def main():
    inp1 = [1, 2, 4, 7, 3, 4, 9, 4, 6, 2]

    print(solution(inp1))


if __name__ == '__main__':
    main()
