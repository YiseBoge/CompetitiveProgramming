def find_substring(string):
    left, result = 0, float("inf")
    counts = [0] * 3
    for right, val in enumerate(string):
        counts[int(val) - 1] += 1
        while counts[int(string[left]) - 1] > 1:
            counts[int(string[left]) - 1] -= 1
            left += 1
        if all(c > 0 for c in counts):
            result = min(result, right - left + 1)
    return result if result < float("inf") else 0


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        results.append(find_substring(input()))
    print(*results, sep="\n")
