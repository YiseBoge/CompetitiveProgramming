from collections import defaultdict


def removables(nums, n):
    mean, counts, result = sum(nums) / n, defaultdict(int), 0
    for num in nums:
        diff = num - mean
        result += counts[-diff]
        counts[diff] += 1
    return result


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1 = int(input())
        inputs = list(map(int, input().split()))
        results.append(removables(inputs, inp1))
    print(*results, sep="\n")
