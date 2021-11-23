def can_sort(nums, n, x):
    left, right = n - x, x
    for i in range(left + 1, right):
        if nums[i] < nums[i - 1]:
            return "NO"

    remaining = list(sorted(nums[:left] + nums[right:]))
    left_big = max(remaining[:left]) if x < n else -float("inf")
    right_small = max(remaining[:left + 1]) if x < n else float("inf")
    return "YES" if left >= right or left_big <= nums[left] <= nums[right - 1] <= right_small else "NO"


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1, inp2 = list(map(int, input().split()))
        inputs = list(map(int, input().split()))
        results.append(can_sort(inputs, inp1, inp2))
    print(*results, sep="\n")
