def make_num(n, m):
    if n >= m:
        return n - m
    steps = 0
    while n < m:
        steps += 1
        n *= 2
    diff = n - m
    limit = 2 ** steps
    while diff:
        while limit > diff:
            limit //= 2
        diff -= limit
        steps += 1
    return steps


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    print(make_num(inp1, inp2))
