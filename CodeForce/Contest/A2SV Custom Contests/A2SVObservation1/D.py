def make_sequence(reds, blues):
    big = [0, 0]
    for i, array in enumerate([reds, blues]):
        prefix = 0
        for num in array:
            prefix += num
            big[i] = max(big[i], prefix)
    return sum(big)


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        _, inputs1 = input(), list(map(int, input().split()))
        _, inputs2 = input(), list(map(int, input().split()))
        results.append(make_sequence(inputs1, inputs2))
    print(*results, sep='\n')
