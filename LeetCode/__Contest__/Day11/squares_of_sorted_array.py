class Solution:
    def sortedSquares(self, A: list) -> list:
        result = []
        left = 0
        right = 0
        for i in range(len(A)):
            if A[i] >= 0:
                left = i - 1
                right = i
                break

        if left == right:
            left = -1
        while 0 <= left or right < len(A):
            if left < 0:
                result.append(A[right] ** 2)
                right += 1
            elif right >= len(A):
                result.append(A[left] ** 2)
                left -= 1
            else:
                if abs(A[left]) <= abs(A[right]):
                    result.append(A[left] ** 2)
                    left -= 1
                else:
                    result.append(A[right] ** 2)
                    right += 1
        return result


def solution(l1):
    s = Solution()
    return s.sortedSquares(l1)


def main():
    inp1 = [-7, -3, 2, 3, 11]

    print(solution(inp1))


if __name__ == '__main__':
    main()
