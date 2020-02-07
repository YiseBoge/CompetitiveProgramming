class Solution:
    def minPathSum(self, grid: list) -> int:
        visited = {}
        return self.do_dfs(grid, (0, 0), visited)

    def do_dfs(self, grid, node, visited):
        if visited.get(node) is not None:
            return visited[node]
        if node == (len(grid) - 1, len(grid[0])):
            return grid[node[0]][node[1]]

        if node[1] + 1 < len(grid[0]) and node[0] + 1 < len(grid):
            result = min(self.do_dfs(grid, (node[0], node[1] + 1), visited)
                         , self.do_dfs(grid, (node[0] + 1, node[1]), visited))
        elif node[1] + 1 < len(grid[0]):
            result = self.do_dfs(grid, (node[0], node[1] + 1), visited)
        elif node[0] + 1 < len(grid):
            result = self.do_dfs(grid, (node[0] + 1, node[1]), visited)
        else:
            result = 0
        visited[node] = result + grid[node[0]][node[1]]
        return visited[node]


def solution(l1):
    s = Solution()
    return s.minPathSum(l1)


def main():
    inp1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    print(solution(inp1))


if __name__ == '__main__':
    main()
