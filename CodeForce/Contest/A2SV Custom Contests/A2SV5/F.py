from collections import deque


def close_roads(edges, stations, n, d):
    graph = [[] for _ in range(n + 1)]
    for one, two in edges:
        graph[one].append(two)
        graph[two].append(one)

    visited, needed = set(stations), set()
    queue = deque((node, 0) for node in visited)
    while queue:
        current, dist = queue.popleft()
        for other in graph[current]:
            if other not in visited:
                visited.add(other)
                needed.add((current, other))
                needed.add((other, current))
                if dist + 1 < d:
                    queue.append((other, dist + 1))
    result = [str(i + 1) for i, edge in enumerate(edges) if tuple(edge) not in needed]
    return str(len(result)) + "\n" + " ".join(result)


if __name__ == "__main__":
    inp1, _, inp2 = list(map(int, input().split()))
    inputs1 = list(map(int, input().split()))
    inputs2 = [list(map(int, input().split())) for _ in range(inp1 - 1)]
    print(close_roads(inputs2, inputs1, inp1, inp2))
