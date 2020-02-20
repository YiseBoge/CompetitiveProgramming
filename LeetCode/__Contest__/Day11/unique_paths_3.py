class Solution:
    def __init__(self):
        self.dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.length = 1

    def uniquePathsIII(self, grid: list) -> int:
        start = (0, 0)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    self.length += 1

        return self.do_dfs(grid, start, set())

    def do_dfs(self, grid, current, visited):
        if grid[current[0]][current[1]] == 2:
            return 1
        visited.add(current)
        result = 0
        for i in self.dir:
            new_i = current[0] + i[0]
            new_j = current[1] + i[1]
            if (0 <= new_i < len(grid) and
                    0 <= new_j < len(grid[0]) and
                    (new_i, new_j) not in visited and
                    (grid[new_i][new_j] == 0 or
                     (grid[new_i][new_j] == 2 and
                      len(visited) == self.length))):
                result += self.do_dfs(grid, (new_i, new_j), visited)

        visited.remove(current)
        return result


def solution(l1):
    s = Solution()
    return s.uniquePathsIII(l1)


def main():
    inp1 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]

    print(solution(inp1))


if __name__ == '__main__':
    main()
