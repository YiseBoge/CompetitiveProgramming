def count_options(a, b, c, m):
    items = list(sorted([a, b, c]))
    small = items[2] - items[0] - items[1] - 1
    big = sum(items) - 3
    return "YES" if small <= m <= big else "NO"


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inputs = list(map(int, input().split()))
        results.append(count_options(*inputs))
    print(*results, sep="\n")
