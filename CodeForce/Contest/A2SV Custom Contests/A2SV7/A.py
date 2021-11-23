def find_winner(reds, blues):
    counts = [0, 0]
    for r, b in zip(reds, blues):
        if r != b:
            counts[int(r < b)] += 1
    if counts[0] == counts[1]:
        return "EQUAL"
    return "RED" if counts[0] > counts[1] else "BLUE"


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        input()
        inp1 = list(map(int, input()))
        inp2 = list(map(int, input()))
        results.append(find_winner(inp1, inp2))
    print(*results, sep="\n")
