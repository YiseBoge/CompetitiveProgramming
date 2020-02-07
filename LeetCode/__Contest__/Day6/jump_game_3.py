class Solution:
    def __init__(self):
        self.visited = set()

    def canReach(self, arr: list, start: int) -> bool:
        self.visited.add(start)
        if arr[start] == 0:
            return True
        result = False

        min_index = start - arr[start]
        max_index = start + arr[start]

        if 0 <= min_index < len(arr) and min_index not in self.visited:
            result = result or self.canReach(arr, min_index)

        if 0 <= max_index < len(arr) and max_index not in self.visited:
            result = result or self.canReach(arr, max_index)

        return result


def solution(l1, l2):
    s = Solution()
    return s.canReach(l1, l2)


def main():
    inp1 = [7, 6, 5, 4, 3, 2, 1]
    inp2 = 3

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
