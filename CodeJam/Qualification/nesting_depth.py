def solution(nums):
    result = []
    opened = 0
    for num in nums:
        diff = num - opened
        # print(diff, result)
        if diff > 0:
            result.append("(" * diff)
        elif diff < 0:
            result.append(")" * -diff)
        result.append(str(num))
        opened += diff

    result.append(")" * opened)
    return "".join(result)


def main():
    length = int(input())

    for i in range(length):
        inp = []
        string = input()
        for s in string:
            inp.append(int(s))
        result = solution(inp)
        print("Case #" + str(i + 1) + ":", result)


if __name__ == "__main__":
    main()
