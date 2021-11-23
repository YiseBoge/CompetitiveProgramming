from collections import deque


def trim_trees(edges, n, k):
    graph, count = [[] for _ in range(n + 1)], [0] * (n + 1)
    for one, two in edges:
        graph[one].append(two)
        graph[two].append(one)
        count[one] += 1
        count[two] += 1
    queue = deque()
    for i in range(1, n + 1):
        if count[i] <= 1:
            queue.append((i, 1))

    result = n
    while queue:
        node, steps = queue.popleft()
        result -= 1
        if steps < k:
            for other in graph[node]:
                count[other] -= 1
                if count[other] == 1:
                    queue.append((other, steps + 1))
    return result


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inputs, _ = [], input()
        inp1, inp2 = list(map(int, input().split()))
        for _ in range(inp1 - 1):
            inputs.append(list(map(int, input().split())))
        results.append(trim_trees(inputs, inp1, inp2))
    print(*results, sep="\n")
