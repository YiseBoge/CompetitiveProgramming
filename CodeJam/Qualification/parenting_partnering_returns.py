def solution(activities):
    res = []
    result = [""] * len(activities)
    held = {"C": None, "J": None}
    acts = [(a, i) for i, a in enumerate(activities)]
    for act, index in sorted(acts):
        current = "C" if len(res) < 1 else res[-1][1]
        if held[current] is None or act[0] >= held[current][1]:
            res.append((index, current))
            held[current] = act
            continue

        new = "J" if current == "C" else "C"
        if held[new] is None or act[0] >= held[new][1]:
            res.append((index, new))
            held[new] = act
            continue
        return "IMPOSSIBLE"

    for ind, val in res:
        result[ind] = val
    return "".join(result)


def main():
    length = int(input())

    for i in range(length):
        inp = []
        size = int(input())
        for _ in range(size):
            inp.append(list(map(int, input().split())))
        result = solution(inp)
        print("Case #" + str(i + 1) + ":", result)


if __name__ == "__main__":
    main()
