from collections import deque


def make_groups(managers, n):
    graph = [[] for _ in range((n + 2))]
    for i, manager in enumerate(managers):
        graph[manager].append(i + 1)
    queue = deque([(-1, 0)])
    while queue:
        current, level = queue.popleft()
        for guy in graph[current]:
            queue.append((guy, level + 1))
    return level


if __name__ == "__main__":
    inp = int(input())
    inputs = [int(input()) for _ in range(inp)]
    print(make_groups(inputs, inp))
