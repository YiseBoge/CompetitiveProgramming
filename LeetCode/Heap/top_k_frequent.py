import heapq


class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        frequencies = {}
        for i in nums:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1
        heap = []
        for i in frequencies:
            if len(heap) < k:
                el = (frequencies[i], i)
                heapq.heappush(heap, el)
            elif frequencies[heap[0][1]] < frequencies[i]:
                el = (frequencies[i], i)
                heapq.heapreplace(heap, el)
        result = []
        for i in heap:
            result.append(i[1])
        return result


def solution(l1, l2):
    s = Solution()
    return s.topKFrequent(l1, l2)


def main():
    inp1 = [-1, 1, 4, -4, 3, 5, 4, -2, 3, -1]
    inp2 = 7
    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
