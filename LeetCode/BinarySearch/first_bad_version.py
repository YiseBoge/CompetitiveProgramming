import sys


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(version):
    return True if version > 5 else False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.findBad(n, 1, n)

    def findBad(self, n, start, finish):
        middle = (start + finish) // 2

        if isBadVersion(middle):
            if middle == 1:
                return 1
            if not isBadVersion(middle - 1):
                return middle

            return self.findBad(n, start, middle - 1)
        else:
            if middle == n:
                return n
            if isBadVersion(middle + 1):
                return middle + 1

            return self.findBad(n, middle + 1, finish)


def solution(l1):
    s = Solution()
    return s.firstBadVersion(l1)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()

    inp1 = 10
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
