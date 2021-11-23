def find_increasing(nums, n):
    start = best = 0
    for end in range(1, n):
        if nums[end] <= nums[end - 1]:
            best = max(best, end - start)
            start = end
    best = max(best, n - start)
    return best


if __name__ == "__main__":
    inp = int(input())
    inputs = list(map(int, input().split()))
    print(find_increasing(inputs, inp))
