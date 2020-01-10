def count_possibilities(moves):
    l_count = 0
    r_count = 0

    for m in moves:
        if m == "L":
            l_count += 1
        else:
            r_count += 1

    return l_count + r_count + 1


def solution(inp):
    return count_possibilities(inp)


def main():
    length = eval(input())

    result = solution(input())

    print(result)


if __name__ == "__main__":
    main()
