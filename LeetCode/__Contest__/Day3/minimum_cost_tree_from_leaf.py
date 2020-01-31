class Solution:
    def mctFromLeafValues(self, arr: list) -> int:
        total = 0

        while len(arr) > 1:
            min_index = 0
            for i in range(len(arr)):
                if arr[i] < arr[min_index]:
                    min_index = i

            min_neighbour = arr[min_index - 1] if min_index == len(arr) - 1 or (
                    min_index > 0 and arr[min_index - 1] < arr[min_index + 1]) else arr[min_index + 1]

            total += min_neighbour * arr[min_index]
            arr.pop(min_index)

        return total


def solution(l1):
    s = Solution()
    return s.mctFromLeafValues(l1)


def main():
    inp1 = [6, 2, 4]

    print(solution(inp1))


if __name__ == '__main__':
    main()
