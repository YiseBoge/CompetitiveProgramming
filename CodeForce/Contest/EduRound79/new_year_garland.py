def check_if_possible(r, g, b):
    if r - 1 > g + b or g - 1 > r + b or b - 1 > r + g:
        return "No"
    return "Yes"


def solution(inp):
    r = eval(inp[0])
    g = eval(inp[1])
    b = eval(inp[2])
    return check_if_possible(r, g, b)


def main():
    inp1 = input()
    length = int(inp1)

    for i in range(length):
        result = solution(input().split())
        print(result)


if __name__ == "__main__":
    main()
