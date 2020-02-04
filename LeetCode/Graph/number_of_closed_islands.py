class Solution:
    def __init__(self):
        self.dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.visited = set()

    def closedIsland(self, grid: list) -> int:
        result = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                val = grid[i][j]
                if val == 0 and (i, j) not in self.visited:
                    if self.do_dfs(grid, (i, j)):
                        result += 1
        return result

    def do_dfs(self, grid, current):
        valid = True
        self.visited.add(current)
        if (current[0] == 0 or current[0] == len(grid) - 1 or
                current[1] == 0 or current[1] == len(grid[0]) - 1):
            valid = False

        for n in self.dir:
            new_i = current[0] + n[0]
            new_j = current[1] + n[1]

            if (0 <= new_i < len(grid) and
                    0 <= new_j < len(grid[0]) and
                    (new_i, new_j) not in self.visited and
                    grid[new_i][new_j] == 0):
                valid = self.do_dfs(grid, (new_i, new_j)) and valid

        return valid


def solution(l1):
    s = Solution()
    return s.closedIsland(l1)


def main():
    inp1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    print(solution(inp1))


if __name__ == '__main__':
    main()
