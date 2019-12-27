def __next(counts, ex):
    res = None

    for i in counts.keys():
        if i is not ex and counts[i] > 0:
            if counts.get(res) is None or (i is not ex and counts[i] > 0 and counts[i] > counts[res]):
                res = i
    return res


def check_if_possible(counts):
    length = counts["R"] + counts["G"] + counts["B"]

    m = None
    for k in range(length):
        m = __next(counts, m)
        if m is None:
            return "No"
        counts[m] -= 1

    return "Yes"


def solution(inp):
    r = eval(inp[0])
    g = eval(inp[1])
    b = eval(inp[2])
    counts = {"R": r, "G": g, "B": b}
    return check_if_possible(counts)


def main():
    inp1 = input()
    length = int(inp1)

    for i in range(length):
        result = solution(input().split())
        print(result)


if __name__ == "__main__":
    main()
