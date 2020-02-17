class Solution:
    def countNegatives(self, grid: list) -> int:
        result = 0

        end = -1
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, end, -1):
                if grid[i][j] < 0:
                    result += 1
                else:
                    end = j
                    break

        return result


def solution(l1):
    s = Solution()
    return s.countNegatives(l1)


def main():
    inp1 = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

    print(solution(inp1))


if __name__ == '__main__':
    main()
