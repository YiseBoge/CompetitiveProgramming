def get_val(before, after):
    letters = ['a', 'b', 'c']
    for i in letters:
        if i != before and i != after:
            return i


def check_beautiful(length, nums):
    collected = {}
    for i in range(length):
        collected[nums[i]] = i

    return None


def solution(inp1, inp2):
    return check_beautiful(inp1, inp2)


def main():
    inp1 = input()
    length = int(inp1)

    result = []
    for i in range(length):
        result += [solution(input(), input().split())]

    print(*result, sep="\n")


if __name__ == "__main__":
    main()
