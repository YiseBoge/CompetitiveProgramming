def find_divisible(l, r):
    x = l
    y = x + x
    if y <= r:
        return str(x) + " " + str(y)


def solution(inp1, inp2):
    return find_divisible(inp1, inp2)


def main():
    inp1 = input()
    length = int(inp1)

    for i in range(length):
        inp = input().split()
        result = solution(int(inp[0]), int(inp[1]))
        print(result)


if __name__ == "__main__":
    main()
