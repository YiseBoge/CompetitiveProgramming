class Solution:
    def maxTurbulenceSize(self, A: list) -> int:
        result = 1
        count = 1
        greater = True
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                if not greater:
                    count += 1
                else:
                    count = 2
                greater = True
            elif A[i] < A[i - 1]:
                if greater:
                    count += 1
                else:
                    count = 2
                greater = False
            else:
                count = 1
            result = max(count, result)
        return result


def solution(l1):
    s = Solution()
    return s.maxTurbulenceSize(l1)


def main():
    inp1 = [9, 4, 2, 10, 7, 8, 8, 1, 9]

    print(solution(inp1))


if __name__ == '__main__':
    main()
