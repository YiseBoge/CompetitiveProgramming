import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def label_graph(edges, n):
    result, graph, degree = {}, [[] for _ in range(n)], [0] * n
    for start, end in edges:
        graph[end - 1].append(start - 1)
        degree[start - 1] += 1

    label = n
    queue = [-node for node in range(n - 1, -1, -1) if degree[node] == 0]
    while queue:
        current = heappop(queue)
        result[-current] = str(label)
        label -= 1
        for new in graph[-current]:
            degree[new] -= 1
            if degree[new] == 0:
                heappush(queue, -new)
    return " ".join(result[node] for node in range(n))


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs = [list(map(int, input().split())) for _ in range(inp2)]
    print(label_graph(inputs, inp1))
