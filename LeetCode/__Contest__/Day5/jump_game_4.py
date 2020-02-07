class Solution:
    def __init__(self):
        self.jumps = {}

    def maxJumps(self, arr: list, d: int) -> int:
        result = 0
        for i in range(len(arr)):
            found = self.count_jumps(arr, d, i) + 1
            result = max(found, result)
        return result

    def count_jumps(self, arr, d, current):
        if self.jumps.get(current):
            return self.jumps[current]
        current_jumps = 0
        min_index = max(current - d, 0)
        max_index = min(current + d, len(arr) - 1)

        r = current + 1
        while r <= max_index and arr[r] < arr[current]:
            possible = self.count_jumps(arr, d, r)
            current_jumps = max(current_jumps, possible + 1)
            r += 1

        l = current - 1
        while l >= min_index and arr[l] < arr[current]:
            possible = self.count_jumps(arr, d, l)
            current_jumps = max(current_jumps, possible + 1)
            l -= 1

        self.jumps[current] = current_jumps
        return current_jumps


def solution(l1, l2):
    s = Solution()
    return s.maxJumps(l1, l2)


def main():
    inp1 = [7, 6, 5, 4, 3, 2, 1]
    inp2 = 3

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
