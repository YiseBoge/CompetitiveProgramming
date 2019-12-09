import sys


def sort_colors(nums) -> None:
    i = 1
    while i < len(nums):
        if nums[i] < nums[i - 1]:
            item = nums[i]
            nums[i] = nums[i - 1]
            nums[i - 1] = item
            if i > 1:
                i -= 1
        else:
            i += 1


def solution(l1):
    sort_colors(l1)
    return l1


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = [2, 0, 2, 1, 1, 0]
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
