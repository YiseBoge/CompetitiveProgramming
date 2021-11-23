def transfer(computers, cables):
    hours, installed = 0, 1
    while installed < cables:
        installed += installed
        hours += 1
    remaining = max(0, computers - installed)
    res, rem = divmod(remaining, cables)
    return hours + res + (rem > 0)


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1, inp2 = list(map(int, input().split()))
        results.append(transfer(inp1, inp2))
    print(*results, sep="\n")
