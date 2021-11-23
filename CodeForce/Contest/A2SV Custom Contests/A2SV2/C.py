def k_multiple_free(nums, k):
    bad, result = set(), 0
    for num in sorted(nums):
        if num not in bad:
            bad.add(k * num)
            result += 1
    return result


def solution(inp1, inp2):
    return k_multiple_free(inp1, inp2)


def main():
    _, inp1 = input().split()
    print(solution(map(int, input().split()), int(inp1)))


if __name__ == "__main__":
    main()
