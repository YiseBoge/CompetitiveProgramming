def get_val(before, after):
    letters = ['a', 'b', 'c']
    for i in letters:
        if i != before and i != after:
            return i


def beautify(ugly):
    result = []
    length = len(ugly)

    if length == 1:
        return get_val(None, None) if ugly[0] == "?" else ugly[0]
    else:
        result.append(get_val(None, ugly[1]) if ugly[0] == "?" else ugly[0])

    for i in range(1, length - 1):
        if ugly[i] == "?":
            result.append(get_val(result[-1], ugly[i + 1]))
        else:
            if ugly[i] == result[-1]:
                return "-1"
            result.append(ugly[i])

    if result[-1] == ugly[-1]:
        return "-1"
    result.append(get_val(None, result[-1]) if ugly[-1] == "?" else ugly[-1])

    return "".join(result)


def solution(inp):
    return beautify(inp)


def main():
    inp1 = input()
    length = int(inp1)

    result = []
    for i in range(length):
        result += [solution(input())]

    print(*result, sep="\n", end="")


if __name__ == "__main__":
    main()
