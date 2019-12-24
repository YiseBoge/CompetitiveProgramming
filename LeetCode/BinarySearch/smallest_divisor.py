import math
import sys


class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        return self.smallFinder(nums, threshold, 1, nums[-1])

    def smallFinder(self, nums, threshold, start, finish):
        middle = (finish + start) // 2

        if self.getSum(nums, middle) > threshold:
            if self.getSum(nums, middle + 1) <= threshold:
                return middle + 1
            return self.smallFinder(nums, threshold, middle + 1, finish)

        if middle > 1:
            if self.getSum(nums, middle - 1) > threshold:
                return middle
            return self.smallFinder(nums, threshold, start, middle - 1)
        return middle

    def getSum(self, nums, divisor):
        result = 0

        for num in nums:
            result += math.ceil(num / divisor)

        return result


def solution(l1, l2):
    s = Solution()
    return s.smallestDivisor(l1, l2)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()

    inp1 = [2, 3, 5, 7, 11]
    inp2 = 10
    sys.stdout.write(str(solution(inp1, inp2)))


if __name__ == '__main__':
    main()
