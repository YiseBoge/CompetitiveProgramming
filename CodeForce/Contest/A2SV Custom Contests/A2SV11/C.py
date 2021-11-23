def make_jumps(string):
    result, end = 0, len(string)
    for i in range(len(string) - 1, -1, -1):
        if string[i] == "R":
            result = max(result, end - i)
            end = i
    return max(result, end + 1)


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        results.append(make_jumps(input()))
    print(*results, sep="\n")
