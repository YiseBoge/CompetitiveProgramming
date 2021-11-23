def discipline(nodes):
    result, n, root = [], len(nodes) + 1, None
    child_respects, disrespect_parent = [False] * n, [False] * n
    for child, val in enumerate(nodes):
        par, resp, child = val[0], val[1], child + 1
        if par == -1:
            root = child
        else:
            child_respects[par] = child_respects[par] or resp == 0
            disrespect_parent[child] = resp == 1

    for node in range(1, n):
        if node != root and disrespect_parent[node] and not child_respects[node]:
            result.append(str(node))
    return " ".join(result) if result else "-1"


if __name__ == "__main__":
    inp, inputs = int(input()), []
    for _ in range(inp):
        inputs.append(list(map(int, input().split())))
    print(discipline(inputs))
