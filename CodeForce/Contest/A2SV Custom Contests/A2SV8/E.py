def make_wins(n, k):
    result = []
    if k < n / 2:
        for i in range(n):
            for j in range(1, k + 1):
                result.append(f"{i + 1} {(i + j) % n + 1}")
    return "-1" if len(result) == 0 else str(len(result)) + "\n" + "\n".join(result)


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    print(make_wins(inp1, inp2))
