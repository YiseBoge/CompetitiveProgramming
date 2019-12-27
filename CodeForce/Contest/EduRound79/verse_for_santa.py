def count_verses(verses, length, maximum):
    verses_count = 0
    biggest_index = 0

    for i in range(length):
        if maximum < verses[i]:
            break
        verses_count += 1
        biggest_index = i if verses[i] > verses[biggest_index] else biggest_index
        maximum -= verses[i]

    # print(verses_count)
    # print(maximum)
    # print("hope is:", maximum + verses[biggest_index])
    # print("currently at:", verses[verses_count])
    if 0 <= verses_count < length:
        if maximum + verses[biggest_index] > verses[verses_count]:
            return biggest_index + 1
        elif verses_count < length - 1 and maximum + verses[verses_count] >= verses[verses_count] + 1:
            return verses_count + 1

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
