class Solution:
    def maxEvents(self, events: list) -> int:
        results = set()
        end_sorted = sorted(events, key=lambda x: x[1])

        for ev in end_sorted:
            for i in range(ev[0], ev[1] + 1):
                if i not in results:
                    results.add(i)
                    break
        return len(results)


def solution(l1):
    s = Solution()
    return s.maxEvents(l1)


def main():
    inp1 = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]

    print(solution(inp1))


if __name__ == '__main__':
    main()
