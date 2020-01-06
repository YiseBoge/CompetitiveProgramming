def gcd(big, small):
    mod = big % small
    if mod == 0:
        return small
    return gcd(small, mod)


def find_fraction(total):
    for i in range(total // 2, 0, -1):
        if gcd(i, total - i) == 1:
            return str(i) + " " + str(total - i)
    return ""


def solution(inp1):
    return find_fraction(inp1)


def main():
    inp1 = input()

    result = solution(int(inp1))
    print(result)


if __name__ == "__main__":
    main()
