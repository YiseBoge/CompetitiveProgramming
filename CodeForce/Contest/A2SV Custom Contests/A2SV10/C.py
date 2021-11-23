def get_score(matrix, m):
    prefix = [[0], [0]]
    for i in range(m):
        prefix[0].append(prefix[0][-1] + matrix[0][i])
        prefix[1].append(prefix[1][-1] + matrix[1][i])

    result = float("inf")
    for i in range(m):
        res = max(prefix[0][-1] - prefix[0][i + 1], prefix[1][i])
        result = min(result, res)
    return result


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1 = int(input())
        inputs = [
            list(map(int, input().split())),
            list(map(int, input().split()))
        ]
        results.append(get_score(inputs, inp1))
    print(*results, sep="\n")
