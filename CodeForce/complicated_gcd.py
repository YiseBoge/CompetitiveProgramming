def complicate_gcd(small, big):
    return small if big == small else 1


def solution(inp1, inp2):
    return complicate_gcd(inp1, inp2)


def main():
    inp = input().split()
    result = solution(inp[0], inp[1])
    print(result)


if __name__ == "__main__":
    main()
