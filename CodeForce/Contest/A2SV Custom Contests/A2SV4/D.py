def underline(letters):
    result, i = 0, 0
    while i < len(letters):
        if letters[i] == "w" or i > 0 and letters[i - 1] == "v":
            result, i = result + 1, i + (i + 1 < len(letters) and letters[i + 1] == "v")
        i += 1
    return result


if __name__ == "__main__":
    inp = int(input())
    results = [underline(input()) for _ in range(inp)]
    print(*results, sep="\n")
