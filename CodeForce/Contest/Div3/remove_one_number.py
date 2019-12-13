def find_maximum(original, length):
    maximum = 1
    count = 1
    removed = False
    sized = False

    for i in range(1, length):
        size = 2 if sized else 1
        # print("maximum:" + str(i))
        # print("i:" + str(i))
        # print("comparing: " + str(original[i-size]) + " with " + str(original[i]))
        if original[i] - original[i - size] == 1:
            count += 1
            sized = False if sized else sized
        else:
            # print("one:" + str(i < (length - 1)))
            # print("two:" + str(not removed))
            # print("three:" + str(original[i+1] - original[i-1] == 1))
            if i < length - 1 and not removed and original[i + 1] - original[i - 1] == 1:
                # print("three:" + str(original[i+1] - original[i-1] == 1))
                i += 1
                removed = True
                sized = True
            else:
                maximum = count if count > maximum else maximum
                count = 1
                removed = False
                sized = False

    maximum = count if count > maximum else maximum

    return maximum


def solution(inp1, inp2):
    return find_maximum(inp1, inp2)


def main():
    inp1 = int(input())
    inp2 = input().split()
    inp2 = list(map(int, inp2))

    print(solution(inp2, inp1))


if __name__ == "__main__":
    main()
