class Solution:
    def minIncrementForUnique(self, A: list) -> int:
        sorted_A = sorted(A)
        moves_count = 0

        for i in range(1, len(sorted_A)):
            num = sorted_A[i]
            prev = sorted_A[i - 1]
            if num <= prev:
                moves_count += prev - num + 1
                sorted_A[i] = prev + 1

        return moves_count


def solution(l1):
    s = Solution()
    return s.minIncrementForUnique(l1)


def main():
    inp1 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

    print(solution(inp1))


if __name__ == '__main__':
    main()
