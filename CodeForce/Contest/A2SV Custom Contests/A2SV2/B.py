def k_dominant(string):
    result, letters = len(string), set(string)
    for letter in letters:
        last, res = -1, -1
        for i, c in enumerate(string):
            if c == letter:
                res = max(res, i - last)
                last = i
        res = max(res, len(string) - last)
        if -1 < res < result:
            result = res
    return result


def solution(inp1):
    return k_dominant(inp1)


def main():
    print(solution(input()))


if __name__ == "__main__":
    main()
