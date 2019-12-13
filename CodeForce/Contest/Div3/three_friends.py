def __pairwise_distance__(friends):
    a1 = abs(friends[0] - friends[1])
    a2 = abs(friends[1] - friends[2])
    a3 = abs(friends[2] - friends[0])
    return a1 + a2 + a3


def make_closer(friends):
    small = min(friends)
    big = max(friends)

    mid = small + ((big - small) // 2)
    # print(friends)
    # print(mid)
    for i in range(3):
        if friends[i] > mid:
            friends[i] -= 1
        elif friends[i] < mid:
            friends[i] += 1

    # print(friends)
    return __pairwise_distance__(friends)


def solution(inp):
    return make_closer(inp)


def main():
    inp1 = input()
    length = int(inp1)

    result = []
    for i in range(length):
        inputs = list(map(int, input().split()))
        result.append(solution(inputs))

    print(*result, sep="\n")


if __name__ == "__main__":
    main()

# 0
# 36
# 0
# 0
# 1999999994
# 1999999994
# 2
# 4
