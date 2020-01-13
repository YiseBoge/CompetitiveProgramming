def is_yasser_happy(length, tastiness):
    total = sum(tastiness)
    count = 0

    for i in range(length - 1):
        count += tastiness[i]
        if count <= 0 or count >= total:
            return "NO"
    return "YES"


def solution(inp1, inp2):
    return is_yasser_happy(inp1, inp2)


def main():
    inp1 = input()
    length = int(inp1)

    for i in range(length):
        inp2 = int(input())
        inp3 = list(map(int, input().split()))
        result = solution(inp2, inp3)
        print(result)


if __name__ == "__main__":
    main()
