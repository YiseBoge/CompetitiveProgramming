def divisible(num):
    def find(end, options):
        nonlocal num
        result = float('inf')
        for ind in range(end, -1, -1):
            if not options:
                break
            if num[ind] in options:
                options.remove(num[ind])
                res = end - ind
                if end == len(num) - 1:
                    new = ["0", "5"] if num[ind] == "0" else ["2", "7"]
                    res += find(ind - 1, new)
                result = min(result, res)
        return result

    return find(len(num) - 1, ["0", "5"])


if __name__ == "__main__":
    inp = int(input())
    results = [divisible(input()) for _ in range(inp)]
    print(*results, sep="\n")
