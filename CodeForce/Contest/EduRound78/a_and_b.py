def operate(num1, num2):
    a = 0
    b = abs(num1 - num2)
    operation_count = 0

    i = 1
    while a != b:
        a = min(a, b)
        b = max(a, b)

        if b - a > ((a + i) - b) + 1:
            a += i
        else:
            b += i

        operation_count += 1
        i += 1

        # if i > 100:
        #     break

    return operation_count


def solution(inp1, inp2):
    return operate(inp1, inp2)


def main():
    inp1 = input()
    length = int(inp1)

    result = []
    for i in range(length):
        inp = input().split()
        result += [solution(int(inp[0]), int(inp[1]))]

    print(*result, sep="\n")


if __name__ == "__main__":
    main()
