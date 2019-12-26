def count_goods(nums, n, p, k):
    goods_count = 0
    all_goods = sorted(nums)

    if n <= k:
        for a in range(n - 1, -1, -1):
            if p >= all_goods[a]:
                return a + 1
    # print(all_goods)
    i = 0
    while i < n and p >= all_goods[i]:
        hope_ind = i + (k - 1)
        # print("index :", i)
        # print("hope :", hope_ind)
        # print("remaining :", p)
        exception = hope_ind + 1 < n and p - all_goods[hope_ind] < all_goods[hope_ind + 1] and p >= all_goods[
            hope_ind + 1] + all_goods[i]

        if hope_ind < n - 1 and p >= all_goods[hope_ind] and not exception:
            # print("Using sale starting between", i, hope_ind)
            goods_count += k
            p -= all_goods[hope_ind]
            i += k
        else:
            # print("Using sale on", i)
            goods_count += 1
            p -= all_goods[i]
            i += 1

    return goods_count


def solution(inp1, inp2):
    return count_goods(inp2, inp1[0], inp1[1], inp1[2])


def main():
    length = eval(input())

    result = []
    for i in range(length):
        inp1 = list(map(int, input().split()))
        inp2 = list(map(int, input().split()))
        result += [solution(inp1, inp2)]
        # print(solution(inp1, inp2))

    print(*result, sep="\n")


if __name__ == "__main__":
    main()

# 6
# 5 6 2
# 2 4 3 5 7
# 5 11 2
# 2 4 3 5 7
# 2 10000 2
# 10000 10000
# 2 9999 2
# 10000 10000
# 5 13 2
# 8 2 8 2 5
# 3 18 2
# 1 2 3


# 3
# 4
# 2
# 0
# 4
# 3
