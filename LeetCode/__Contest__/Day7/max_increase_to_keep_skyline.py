class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list) -> int:
        result = 0
        rows_max = [-1] * len(grid)
        cols_max = [-1] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid)):
                r_max = rows_max[i]
                if r_max < 0:
                    r_max = max(grid[i])
                    rows_max[i] = r_max

                c_max = cols_max[j]
                if c_max < 0:
                    for row in grid:
                        c_max = max(c_max, row[j])
                    cols_max[j] = c_max
                result += min(r_max, c_max) - grid[i][j]
        return result


def solution(l1):
    s = Solution()
    return s.maxIncreaseKeepingSkyline(l1)


def main():
    inp1 = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]

    print(solution(inp1))


if __name__ == '__main__':
    main()
