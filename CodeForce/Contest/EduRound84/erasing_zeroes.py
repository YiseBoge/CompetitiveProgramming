def erase_zeroes(string):
    started = False
    removal_count = 0
    for i in string:
        if i == "1":
            started = True
        elif started:
            removal_count += 1

    if not started:
        return 0

    end_count = 0
    for i in range(len(string) - 1, -1, -1):
        if string[i] == "1":
            break
        end_count += 1

    return removal_count - end_count


def solution(inp1):
    return erase_zeroes(inp1)


def main():
    inp1 = input()
    length = int(inp1)

    for i in range(length):
        inp1 = input()
        result = solution(inp1)
        print(result)


if __name__ == "__main__":
    main()
