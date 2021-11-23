def make_words(commons, n):
    result = ["a" * max(1, commons[0])]
    for i, common in enumerate(commons):
        candidate = result[-1][:common]
        candidate += "b" if common < len(result[-1]) and result[-1][common] == "a" else "a"

        if i < n - 1 and len(candidate) < commons[i + 1]:
            candidate += "a" * (commons[i + 1] - len(candidate))
        result.append(candidate)
    return "\n".join(result)


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1 = int(input())
        inputs = list(map(int, input().split()))
        results.append(make_words(inputs, inp1))
    print(*results, sep="\n")
