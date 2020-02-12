import math


def repair_road(n, g, b):
    half = math.ceil(n / 2)
    cycles = math.ceil(half / g)
    t = (cycles - 1) * g + (cycles - 1) * b
    r = half % g
    total = t + r if r > 0 else t + g
    return max(n, total)


def solution(inp1):
    n = inp1[0]
    g = inp1[1]
    b = inp1[2]
    return repair_road(n, g, b)


def main():
    inp1 = input()
    length = int(inp1)

    for i in range(length):
        inp1 = list(map(int, input().split()))
        result = solution(inp1)
        print(result)


if __name__ == "__main__":
    main()
