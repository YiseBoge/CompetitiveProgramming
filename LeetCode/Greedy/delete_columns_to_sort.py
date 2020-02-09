class Solution:
    def minDeletionSize(self, A: list) -> int:
        deletion_count = 0

        for i in range(len(A[0])):
            prev = A[0][i]
            for string in A:
                if string[i] < prev:
                    deletion_count += 1
                    break
                prev = string[i]

        return deletion_count


def solution(l1):
    s = Solution()
    return s.minDeletionSize(l1)


def main():
    inp1 = ["zyx", "wvu", "tsr"]

    print(solution(inp1))


if __name__ == '__main__':
    main()
