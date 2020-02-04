class Solution:
    def findCircleNum(self, M: list) -> int:
        result = 0
        visited = set()

        for i in range(len(M)):
            if i not in visited:
                self.do_dfs(M, i, visited)
                result += 1

        return result

    def do_dfs(self, grid, current, visited):
        visited.add(current)
        for f in range(len(grid)):
            if f not in visited and grid[current][f] == 1:
                self.do_dfs(grid, f, visited)


def solution(l1):
    s = Solution()
    return s.findCircleNum(l1)


def main():
    inp1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    print(solution(inp1))


if __name__ == '__main__':
    main()
