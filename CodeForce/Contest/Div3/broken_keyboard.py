def tell(original, keys):
    print(original)
    print(keys)
    return len(original)


def solution(inp, inp2):
    return tell(inp, inp2)


def main():
    input().split()
    inp2 = input()
    inp3 = input().split()

    print(solution(inp2, inp3), end="")


if __name__ == "__main__":
    main()
