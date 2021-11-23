import sys
from heapq import heappop, heappush


def understand(requirements, n):
    degree, graph = [0] * n, [[] for _ in range(n)]
    for i, req in enumerate(requirements):
        degree[i] += len(req)
        for r in req:
            graph[r - 1].append(i)

    finished = 0
    queue = [(1, i) for i, d in enumerate(degree) if d == 0]
    while queue:
        time, current = heappop(queue)
        finished += 1
        for chapter in graph[current]:
            degree[chapter] -= 1
            if degree[chapter] == 0:
                heappush(queue, (time + (current > chapter), chapter))
    return str(time if finished == n else -1)


if __name__ == "__main__":
    inp, results = int(sys.stdin.readline()), []
    for _ in range(inp):
        inp1 = int(sys.stdin.readline())
        inputs = []
        for _ in range(inp1):
            inputs.append(list(map(int, sys.stdin.readline().split()[1:])))
        results.append(understand(inputs, inp1))
    sys.stdout.write("\n".join(results))
