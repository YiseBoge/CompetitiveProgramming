import sys


class Solution:
    def search(self, nums, target: int) -> int:
        return self.searcher(nums, target, 0, len(nums) - 1)

    def searcher(self, nums, target, start, finish) -> int:

        if finish < start:
            return -1

        middle = (finish + start) // 2
        val = nums[middle]

        if target < val:
            return self.searcher(nums, target, start, middle - 1)
        if target > val:
            return self.searcher(nums, target, middle + 1, finish)

        return middle


def solution(l1, l2):
    s = Solution()
    return s.search(l1, l2)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()

    inp1 = [-1, 0, 3, 5, 9, 12]
    inp2 = -1
    sys.stdout.write(str(solution(inp1, inp2)))


if __name__ == '__main__':
    main()
