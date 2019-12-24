def find_no_coverage_time(a, b, c, r):
    maximum = max(a, b)
    minimum = min(a, b)

    lowest_range = max(minimum, c - r)
    highest_range = min(maximum, c + r)

    full_trip = maximum - minimum
    covered_trip = highest_range - lowest_range

    if highest_range < minimum or lowest_range > maximum:
        return full_trip
    return full_trip - covered_trip


def solution(inp):
    return find_no_coverage_time(inp[0], inp[1], inp[2], inp[3])


def main():
    length = eval(input())

    result = []
    for i in range(length):
        result += [solution(list(map(int, input().split())))]

    print(*result, sep="\n")


if __name__ == "__main__":
    main()

# 7
# 0
# 4
# 0
# 30
# 5
# 4
# 0
# 3
