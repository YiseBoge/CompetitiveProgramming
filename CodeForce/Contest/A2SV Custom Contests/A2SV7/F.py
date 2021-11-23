from collections import defaultdict


def count_edges(edges, queries, n):
    sorted_queries, ind, query_map = list(sorted(queries)), 0, defaultdict(int)
    root, size = list(range(n + 1)), [1] * (n + 1)
    result = 0

    def find(node):
        if root[node] != node:
            root[node] = find(root[node])
        return root[node]

    def union(node1, node2):
        nonlocal result
        small, big = tuple(sorted([find(node1), find(node2)], key=lambda x: size[x]))
        if small != big:
            root[small] = big
            result += size[small] * size[big]
            size[big] += size[small]

    for start, end, weight in sorted(edges, key=lambda x: x[2]):
        if ind < len(sorted_queries) and weight > sorted_queries[ind]:
            query_map[sorted_queries[ind]] = result
            ind += 1
        union(start, end)
    for i in range(ind, len(queries)):
        query_map[sorted_queries[i]] = result
    return " ".join(str(query_map[q]) for q in queries)


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs1 = []
    for _ in range(inp1 - 1):
        inputs1.append(list(map(int, input().split())))
    inputs2 = list(map(int, input().split()))
    print(count_edges(inputs1, inputs2, inp1))
