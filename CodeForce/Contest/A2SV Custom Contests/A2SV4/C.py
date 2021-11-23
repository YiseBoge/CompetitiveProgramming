def distribute(group_list, n, m):
    root, group, size = list(range(m)), [[] for _ in range(n + 1)], [1] * m

    def find(node):
        if root[node] != node:
            root[node] = find(root[node])
        return root[node]

    def union(node1, node2):
        small, big = tuple(sorted([find(node1), find(node2)], key=lambda x: size[x]))
        root[small] = big
        size[big] += size[small]

    for i, g in enumerate(group_list):
        for person in g:
            group[person].append(i)

    for g in group:
        for i in range(1, len(g)):
            union(g[i], g[i - 1])
    result = [str(size[find(g[0])] + 1) if g else "1" for g in group[1:]]
    return " ".join(result)


if __name__ == "__main__":
    inp = input().split()
    inp1, inp2 = int(inp[0]), int(inp[1])
    inputs = []
    for _ in range(inp2):
        inputs.append(list(map(int, input().split()[1:])))
    print(distribute(inputs, inp1, inp2))
