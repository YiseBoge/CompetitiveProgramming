def make_zero(num):
    result = sum(1 + int(c) for c in num[:-1] if c != "0")
    return result + int(num[-1])


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        input()
        results.append(make_zero(input()))
    print(*results, sep="\n")
