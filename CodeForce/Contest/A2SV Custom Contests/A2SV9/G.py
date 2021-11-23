from collections import deque


def beautify(beauty, edges, n):
    tree = [[] for _ in range(n)]
    biggest, big_val = (-1, -1), -1
    for one, two in edges:
        tree[one - 1].append(two - 1)
        tree[two - 1].append(one - 1)
        l1, r1 = beauty[one - 1]
        l2, r2 = beauty[two - 1]
        diff = max(abs(r2 - l1), abs(r1 - l2))
        if diff > big_val:
            biggest, big_val = (one - 1, two - 1), diff
    queue = deque()
    l1, r1 = beauty[biggest[0] - 1]
    l2, r2 = beauty[biggest[1] - 1]
    a, b = abs(r2 - l1), abs(r1 - l2)
    if a >= b:
        queue.append((biggest[0], beauty[biggest[0]][1]))
        queue.append((biggest[1], beauty[biggest[1]][0]))
    else:
        queue.append((biggest[0], beauty[biggest[0]][0]))
        queue.append((biggest[1], beauty[biggest[1]][1]))
    visited = set(biggest)

    while queue:
        current, picked = queue.popleft()
        for new in tree[current]:
            if new not in visited:
                visited.add(new)
                l, r = beauty[new]
                new_pick = l if abs(picked - l) > abs(picked - r) else r
                big_val += abs(picked - new_pick)
                queue.append((new, new_pick))
    return big_val


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inputs1, inputs2 = [], []
        inp1 = int(input())
        for _ in range(inp1):
            inputs1.append(list(map(int, input().split())))
        for _ in range(inp1 - 1):
            inputs2.append(list(map(int, input().split())))
        results.append(beautify(inputs1, inputs2, inp1))
    print(*results, sep="\n")
