def find_maximum(students):
    sorted_value = list(sorted(students))
    left = result = 0
    for right, val in enumerate(sorted_value):
        while left < right and val - 5 > sorted_value[left]:
            left += 1
        result = max(result, right - left + 1)
    return result


def solution(inp1):
    return find_maximum(inp1)


def main():
    _ = int(input())
    print(solution(map(int, input().split())))


if __name__ == "__main__":
    main()
