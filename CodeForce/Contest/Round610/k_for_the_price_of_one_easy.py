def count_goods(nums, n, p, k):
    goods_count = 0
    all_goods = sorted(nums)

    if n <= k:
        for a in range(n - 1, -1, -1):
            if p >= all_goods[a]:
                return a + 1

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
        if p >= s or (i + 1 < 2 * k and p >= current):
            p -= all_goods[i]
            del all_goods[(i - k) + 1: i + 1]
            n -= k
            goods_count += k
            # print("********bought from ", (i - k) + 1, "to", i)
            i = i - k
            continue
        i -= 1

    # print(all_goods)
    if len(all_goods) >= k and all_goods[k - 1] <= p:
        goods_count += k
        p -= all_goods[k - 1]
        del all_goods[:k]
        n -= 1

    # print(all_goods)
    while len(all_goods) > 0 and all_goods[0] <= p:
        goods_count += 1
        p -= all_goods[0]
        del all_goods[0]
        n -= 1

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
