import sys


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def solution(numbers, tar):
    return two_sum(numbers, tar)


def main():
    inp = sys.stdin.readline().split()
    in1 = inp[0]
    numbers = [0, 634, 34, 5]
    sys.stdout.write(str(solution(numbers, int(in1))))


if __name__ == '__main__':
    main()
