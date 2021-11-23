from collections import Counter


def improve_array(nums, n, k):
    requirements = Counter([k - (num % k) for num in nums])
    big = 0
    for requirement, count in requirements.items():
        if requirement < k:
            big = max(big, (count - 1) * k + requirement + 1)
    return big


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1, inp2 = list(map(int, input().split()))
        inputs = list(map(int, input().split()))
        results.append(improve_array(inputs, inp1, inp2))
    print(*results, sep="\n")
