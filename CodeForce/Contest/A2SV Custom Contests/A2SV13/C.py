from heapq import heappop, heappush


def record_nodes(edges, n):
    graph = [[] for _ in range(n + 1)]
    for one, two in edges:
        graph[one].append(two)
        graph[two].append(one)
    queue, result, visited = [1], [], set()
    while queue:
        current = heappop(queue)
        if current not in visited:
            visited.add(current)
            result.append(str(current))
            for other in graph[current]:
                if other not in visited:
                    heappush(queue, other)
    return " ".join(result)


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs = [list(map(int, input().split())) for _ in range(inp2)]
    print(record_nodes(inputs, inp1))
