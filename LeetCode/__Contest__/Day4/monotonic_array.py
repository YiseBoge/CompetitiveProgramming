class Solution:
    def isMonotonic(self, A: list) -> bool:
        result = True
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                result = False
                break

        if result:
            return result
        result = True

        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                result = False
                break

        return result


def solution(l1):
    s = Solution()
    return s.isMonotonic(l1)


def main():
    inp1 = [6, 2, 4]

    print(solution(inp1))


if __name__ == '__main__':
    main()
