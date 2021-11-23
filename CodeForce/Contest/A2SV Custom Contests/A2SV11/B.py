def add_walks(walks, n, k):
    added = 0
    for i in range(1, n):
        rem = max(0, k - walks[i] - walks[i - 1])
        added += rem
        walks[i] += rem
    return f"{added}\n" + " ".join(map(str, walks))


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs = list(map(int, input().split()))
    print(add_walks(inputs, inp1, inp2))
