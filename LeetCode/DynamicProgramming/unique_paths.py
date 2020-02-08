class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths_count = {(n - 1, m - 1): 1}
        start = (0, 0)
        self.do_dfs(start, m, n, paths_count)
        return paths_count[start]

    def do_dfs(self, current, m, n, paths_count):
        if current in paths_count:
            return paths_count[current]
        down = (current[0] + 1, current[1])
        right = (current[0], current[1] + 1)
        result = 0

        if down[0] < n:
            result += self.do_dfs(down, m, n, paths_count)
        if right[1] < m:
            result += self.do_dfs(right, m, n, paths_count)

        paths_count[current] = result
        return result


def solution(l1, l2):
    s = Solution()
    return s.uniquePaths(l1, l2)


def main():
    inp1 = 12
    inp2 = 3

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
