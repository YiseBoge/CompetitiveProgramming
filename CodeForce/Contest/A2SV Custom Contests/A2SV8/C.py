def count_pairs(nums, left, right):
    nums.sort()
    result = 0
    for i, num in enumerate(nums):
        start, end, res1 = i + 1, len(nums) - 1, len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] + num >= left:
                res1, end = mid, mid - 1
            else:
                start = mid + 1

        start, end, res2 = i + 1, len(nums) - 1, -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] + num <= right:
                res2, start = mid, mid + 1
            else:
                end = mid - 1
        result += max(0, res2 - res1 + 1)
    return result


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        _, inp1, inp2 = list(map(int, input().split()))
        inputs = list(map(int, input().split()))
        results.append(count_pairs(inputs, inp1, inp2))
    print(*results, sep="\n")
