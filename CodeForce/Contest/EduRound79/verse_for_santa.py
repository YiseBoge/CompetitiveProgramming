def count_verses(verses, length, maximum):
    biggest_index = 0

    i = 0
    while i < length and maximum >= 0:
        biggest_index = i if verses[i] > verses[biggest_index] else biggest_index
        maximum -= verses[i]
        i += 1

    if maximum < 0:
        return biggest_index + 1
    return 0


def solution(inp1, inp2):
    length = inp1[0]
    maximum = inp1[1]
    return count_verses(inp2, length, maximum)


def main():
    inp1 = input()
    length = int(inp1)

    for i in range(length):
        inp1 = list(map(int, input().split()))
        inp2 = list(map(int, input().split()))
        result = solution(inp1, inp2)
        print(result)


if __name__ == "__main__":
    main()
