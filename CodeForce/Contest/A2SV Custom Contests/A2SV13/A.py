def save_mice(mice, n, m):
    mice.sort()
    cat_place, ind = 0, m - 1
    while ind >= 0 and cat_place < mice[ind]:
        cat_place += n - mice[ind]
        ind -= 1
    return m - ind - 1


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1, inp2 = list(map(int, input().split()))
        inputs = list(map(int, input().split()))
        results.append(save_mice(inputs, inp1, inp2))
    print(*results, sep="\n")
