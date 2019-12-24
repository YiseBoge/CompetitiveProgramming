def count_goods(nums, n, p, k):
    goods_count = 0
    all_goods = sorted(nums)

    if n <= k:
        for a in range(n - 1, -1, -1):
            if p >= all_goods[a]:
                return a + 1

    # while k > 1 and n > 0:
    #     # loop content would have gone here
    #
    #     k -= 1
    #     # print("_______restarting with new k _________", k)

    i = n - 1
    while i >= k:
        # print(all_goods)
        # print("n is", n, "and k is", k)
        # print("count is", goods_count)
        # print("index is", i)
        # print("remaining is", p)
        current = all_goods[i]
        hope = all_goods[i - k]
        s = current + hope
        if p >= s or i + 1 < 2 * k and p >= current:
            p -= all_goods[i]
            del all_goods[(i - k) + 1: i + 1]
            n -= k
            goods_count += k
            # print("********bought from ", (i - k) + 1, "to", i)
            i = i - k
            continue
        i -= 1

    # print(all_goods)
    while len(all_goods) > 0 and all_goods[0] <= p:
        goods_count += 1
        p -= all_goods[0]
        del all_goods[0]

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

# 8
# 5 6 2
# 2 4 3 5 7
# 5 11 2
# 2 4 3 5 7
# 3 2 3
# 4 2 6
# 5 2 3
# 10 1 3 9 2
# 2 10000 2
# 10000 10000
# 2 9999 2
# 10000 10000
# 4 6 4
# 3 2 3 2
# 5 5 3
# 1 2 2 1 2


# 3
# 4
# 1
# 1
# 2
# 0
# 4
# 5
