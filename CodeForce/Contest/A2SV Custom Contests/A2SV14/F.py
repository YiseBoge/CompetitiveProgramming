def rescue_love(valya, tolya):
    root, size = list(range(26)), [1] * 26

    def find(node):
        if root[node] != node:
            root[node] = find(root[node])
        return root[node]

    def union(node1, node2):
        small, big = tuple(sorted([find(node1), find(node2)], key=lambda x: size[x]))
        root[small] = big
        size[big] += size[small]

    result = []
    for v, t in zip(valya, tolya):
        ind1, ind2 = ord(v) - ord("a"), ord(t) - ord("a")
        if find(ind1) != find(ind2):
            result.append(f"{v} {t}")
            union(ind1, ind2)
    return f"{len(result)}\n" + "\n".join(result)


if __name__ == "__main__":
    _ = input()
    inp1, inp2 = input(), input()
    print(rescue_love(inp1, inp2))
