def subtract_prime(big, small):
    if big - small > 1:
        return "YES"
    return "NO"


def solution(inp1, inp2):
    return subtract_prime(inp1, inp2)


def main():
    inp1 = input()
    length = int(inp1)

    for i in range(length):
        inp = input().split()
        result = solution(int(inp[0]), int(inp[1]))
        print(result)


if __name__ == "__main__":
    main()
