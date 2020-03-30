def get_val(before, after):
    letters = ['a', 'b', 'c']
    for i in letters:
        if i != before and i != after:
            return i


def check_beautiful(perm):
    pos = [0 for i in range(len(perm) + 1)]
    for i in range(len(perm)):
        pos[int(perm[i])] = i
    result = []
    max = pos[1]
    min = pos[1]
    for i in range(1, len(perm) + 1):
        if max < pos[i]:
            max = pos[i]
        elif min > pos[i]:
            min = pos[i]
        if max - min + 1 > i:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)


def solution(inp1):
    return check_beautiful(inp1)


def main():
    inp1 = input()
    length = int(inp1)

    result = []
    for i in range(length):
        input()
        result += [solution(input().split())]

    print(*result, sep="\n")


if __name__ == "__main__":
    main()
