def is_yasser_happy(length, tastiness):
    total = sum(tastiness)
    count = total

    start = 0
    end = length - 1
    while True:
        if tastiness[start] <= tastiness[end]:
            count -= tastiness[start]
            start += 1
        else:
            count -= tastiness[end]
            end -= 1

        if count >= total:
            return "NO"
        if start > end:
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
