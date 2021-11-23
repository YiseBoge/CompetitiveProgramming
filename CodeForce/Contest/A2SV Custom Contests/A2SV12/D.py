import sys

input = sys.stdin.readline


def buy_presents(friends, cost, n, m):
    result = ind = 0
    for k in sorted(friends, reverse=True):
        result += cost[min(ind, k - 1)]
        ind += ind <= k
    return result


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1, inp2 = list(map(int, input().split()))
        inputs1 = list(map(int, input().split()))
        inputs2 = list(map(int, input().split()))
        results.append(buy_presents(inputs1, inputs2, inp1, inp2))
    print(*results, sep="\n")
