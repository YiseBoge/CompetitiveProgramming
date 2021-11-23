import sys

input = sys.stdin.readline


def validate_religions(universe, queries, n):
    religions, before, result = [[], [], []], [[-1] * 26], []

    for i, u in enumerate(universe):
        before.append(list(before[-1]))
        before[-1][ord(u) - ord("a")] = i

    for query in queries:
        op, ind = query[0], int(query[2]) - 1
        if op == "-":
            religions[ind].pop()
        else:
            religions[ind].append(query[-1])

        print(religions)
        visited = set()
        for religion in religions:
            ind = before[n][ord(religion[-1]) - ord("a")] if len(religion) else ""
            for r in religion[::-1]:
                index = ord(r) - ord("a")
                while ind in visited:
                    ind = before[ind][index]
                if ind < 0:
                    result.append("NO")
                    break
                visited.add(ind)
            else:
                continue
            break
        else:
            result.append("YES")

    return "\n".join(result)


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs1 = input().strip()
    inputs2 = [input().strip() for _ in range(inp2)]
    print(validate_religions(inputs1, inputs2, inp1))
