def add_edges(mocha, diana, n):
    mocha_root, diana_root = list(range(n + 1)), list(range(n + 1))
    mocha_size, diana_size = [1] * (n + 1), [1] * (n + 1)

    def find(node, root):
        if root[node] != node:
            root[node] = find(root[node], root)
        return root[node]

    def union(node1, node2, root, size):
        small, big = tuple(sorted([find(node1, root), find(node2, root)], key=lambda x: size[x]))
        root[small] = big
        size[big] += size[small]

    for one, two in mocha:
        union(one, two, mocha_root, mocha_size)
    for one, two in diana:
        union(one, two, diana_root, diana_size)

    result = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (find(i, mocha_root) != find(j, mocha_root) and
                    find(i, diana_root) != find(j, diana_root)):
                result.append(f"{i} {j}")
                union(i, j, mocha_root, mocha_size)
                union(i, j, diana_root, diana_size)
    return str(len(result)) + "\n" + "\n".join(result)


if __name__ == "__main__":
    inp = input().split()
    inp1, inp2, inp3 = int(inp[0]), int(inp[1]), int(inp[2])
    inputs1, inputs2 = [], []
    for _ in range(inp2):
        inputs1.append(list(map(int, input().split())))
    for _ in range(inp3):
        inputs2.append(list(map(int, input().split())))
    print(add_edges(inputs1, inputs2, inp1))
