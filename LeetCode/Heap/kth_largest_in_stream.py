import heapq


class KthLargest:

    def __init__(self, k: int, nums: list):
        self.heap = []
        self.k = k
        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i)
            elif i > self.heap[0]:
                heapq.heapreplace(self.heap, i)
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


def main():
    obj = KthLargest(3, [4, 5, 8, 2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(6))


if __name__ == '__main__':
    main()
