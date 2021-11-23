import sys

input = sys.stdin.readline


def make_one(nums):
    negative_count = zero_count = result = 0
    for num in nums:
        negative_count = (negative_count + (num < 0)) % 2
        if num == 0:
            zero_count += 1
        else:
            result += abs(num) - 1
    result += 2 * negative_count * (zero_count == 0)
    result += zero_count
    return result


if __name__ == "__main__":
    inp = int(input())
    print(make_one(list(map(int, input().split()))))
