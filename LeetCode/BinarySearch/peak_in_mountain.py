import sys


class Solution:
    def peakIndexInMountainArray(self, A) -> int:
        return self.peakFinder(A, 0, len(A) - 1)

    def peakFinder(self, lst, start, finish):

        middle = (finish + start) // 2
        # print(middle)

        if middle > 0 and lst[middle - 1] > lst[middle]:
            return self.peakFinder(lst, start, middle - 1)
        if middle < len(lst) - 1 and lst[middle + 1] > lst[middle]:
            return self.peakFinder(lst, middle + 1, finish)

        return middle


def solution(l1):
    s = Solution()
    return s.peakIndexInMountainArray(l1)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()

    inp1 = [0, 1, 2, 1, 0]
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
