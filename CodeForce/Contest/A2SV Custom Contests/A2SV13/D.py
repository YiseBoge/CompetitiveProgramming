from collections import deque


def block_bad(grid, m, n):
    dirs = [0, 1, 0, -1, 0]
    good_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "G":
                good_count += 1
            elif grid[i][j] == "B":
                for d in range(4):
                    new_i, new_j = i + dirs[d], j + dirs[d + 1]
                    if 0 <= new_i < m and 0 <= new_j < n:
                        if grid[new_i][new_j] == "G":
                            return "NO"
                        if grid[new_i][new_j] != "B":
                            grid[new_i][new_j] = "#"

    queue, visited, found = deque(), set(), 0
    start = (m - 1, n - 1)
    if grid[m - 1][n - 1] == ".":
        queue.append(start)
        visited.add(start)
    while queue:
        i, j = queue.popleft()
        found += grid[i][j] == "G"
        for d in range(4):
            new = new_i, new_j = i + dirs[d], j + dirs[d + 1]
            if (0 <= new_i < m and 0 <= new_j < n and
                    new not in visited and grid[new_i][new_j] != "#"):
                visited.add(new)
                queue.append(new)
    return "YES" if good_count == found else "NO"


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1, inp2 = list(map(int, input().split()))
        inputs = [list(input()) for _ in range(inp1)]
        results.append(block_bad(inputs, inp1, inp2))
    print(*results, sep="\n")
