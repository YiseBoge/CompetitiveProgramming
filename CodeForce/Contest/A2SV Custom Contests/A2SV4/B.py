def build(districts):
    result, options = [], [0]
    for i, gang in enumerate(districts):
        if districts[options[0]] != gang:
            options.append(i)
            break
    if len(options) < 2:
        return "NO"

    result = ["YES"]
    for i in range(1, len(districts)):
        opt = options[districts[i] == districts[options[0]]]
        result.append(f"{opt + 1} {i + 1}")
    return "\n".join(result)


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        input()
        results.append(build(input().split()))
    print(*results, sep="\n")
