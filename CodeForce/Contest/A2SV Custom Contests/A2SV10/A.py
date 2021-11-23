def find_indices(nums):
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return f"YES\n{i} {i + 1} {i + 2}"
    return "NO"


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        input()
        results.append(find_indices(list(map(int, input().split()))))
    print(*results, sep="\n")
