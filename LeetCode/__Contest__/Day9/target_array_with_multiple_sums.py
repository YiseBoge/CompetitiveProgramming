import heapq


class Solution:
    def isPossible(self, target: list) -> bool:
        heap = []
        for i in target:
            heap.append(-i)
        heapq.heapify(heap)
        total = sum(target)

        while True:
            if heap[0] == -1:
                return True
            current = -heapq.heappop(heap)
            reducable = total - current
            current = current - reducable
            total = reducable + current
            # print(heap, current, total)
            if current < 1:
                return False
            heapq.heappush(heap, -current)


def solution(l1):
    s = Solution()
    return s.isPossible(l1)


def main():
    inp1 = [9, 3, 5]

    print(solution(inp1))


if __name__ == '__main__':
    main()
