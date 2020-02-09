class Solution:
    def eraseOverlapIntervals(self, intervals: list) -> int:
        if not intervals: return 0
        interval = sorted(intervals, key=lambda i: i[1])
        count = 0
        time_min = interval[0][0]
        for i in interval:
            if time_min <= i[0]:
                count += 1
                time_min = i[1]
        return len(intervals) - count


def solution(l1):
    s = Solution()
    return s.eraseOverlapIntervals(l1)


def main():
    inp1 = [[1000, 20], [30, 20], [400, 50], [30, 20], [1, 1], [30, 20]]

    print(solution(inp1))


if __name__ == '__main__':
    main()
