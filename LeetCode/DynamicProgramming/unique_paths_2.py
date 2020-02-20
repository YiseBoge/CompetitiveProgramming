class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        start = (0, 0)
        end = (len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)
        if obstacleGrid[start[0]][start[1]] == 1 or obstacleGrid[end[0]][end[1]] == 1:
            return 0
        paths_count = {end: 1}
        self.do_dfs(start, obstacleGrid, paths_count)
        return paths_count[start]

    def do_dfs(self, current, grid, paths_count):
        if current in paths_count:
            return paths_count[current]
        down = (current[0] + 1, current[1])
        right = (current[0], current[1] + 1)
        result = 0

        if down[0] < len(grid) and grid[down[0]][down[1]] == 0:
            result += self.do_dfs(down, grid, paths_count)
        if right[1] < len(grid[0]) and grid[right[0]][right[1]] == 0:
            result += self.do_dfs(right, grid, paths_count)

        paths_count[current] = result
        return result


def solution(l1):
    s = Solution()
    return s.uniquePathsWithObstacles(l1)


def main():
    inp1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    print(solution(inp1))


if __name__ == '__main__':
    main()
