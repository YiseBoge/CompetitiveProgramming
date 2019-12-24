import sys


class Solution:
    def hIndex(self, citations) -> int:
        if len(citations) == 0:
            return 0
        return self.finder(citations, 0, len(citations) - 1)

    def finder(self, citations, start, finish):
        middle = (start + finish) // 2
        val = citations[middle]
        ind = (len(citations) - 1) - middle

        if finish < start:
            return ind
        if val > ind:
            return self.finder(citations, start, middle - 1)
        if val < ind:
            return self.finder(citations, middle + 1, finish)

        return ind


def solution(l1):
    s = Solution()
    return s.hIndex(l1)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()

    inp1 = [0, 1, 2, 3, 6]
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
