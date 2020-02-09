class Solution:
    def minimumTotal(self, triangle: list) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            row = triangle[i]
            next_row = triangle[i + 1]
            for j in range(len(row)):
                row[j] += min(next_row[j], next_row[j + 1])

        return triangle[0][0]


def solution(l1):
    s = Solution()
    return s.minimumTotal(l1)


def main():
    inp1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

    print(solution(inp1))


if __name__ == '__main__':
    main()
