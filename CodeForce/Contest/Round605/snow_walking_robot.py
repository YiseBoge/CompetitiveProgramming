def __equalize__(moves):
    a = moves["L"]
    b = moves["R"]
    c = moves["U"]
    d = moves["D"]
    moves["L"] = moves["R"] = min(a, b)
    moves["U"] = moves["D"] = min(c, d)

    if moves["U"] == 0 and moves["L"] > 1:
        moves["L"] = moves["R"] = 1
    if moves["R"] == 0 and moves["U"] > 1:
        moves["U"] = moves["D"] = 1


def __move__(start, move):
    if move == "L":
        return start[0] - 1, start[1]
    elif move == "R":
        return start[0] + 1, start[1]
    elif move == "U":
        return start[0], start[1] + 1
    elif move == "D":
        return start[0], start[1] - 1


def correct(path):
    moves = {"L": 0, "U": 0, "R": 0, "D": 0}
    results = []

    for i in path:
        moves[i] += 1
    __equalize__(moves)
    moves_count = moves["L"] + moves["U"] + moves["R"] + moves["D"]

    if moves_count > 0:
        for i in moves:
            results += [i] * moves[i]

    result = "".join(results)

    return str(moves_count), result


def solution(inp):
    return correct(inp)


def main():
    inp1 = input()
    length = int(inp1)

    result = []
    for i in range(length):
        s = solution(input())
        result.append(s[0])
        if int(s[0]) > 0:
            result.append(s[1])

    print(*result, sep="\n")


if __name__ == "__main__":
    main()

# 2
# LR
# 14
# RUURDDDDLLLUUR
# 12
# ULDDDRRRUULL
# 2
# LR
# 2
# UD
# 0
