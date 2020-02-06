class Solution:
    def kWeakestRows(self, mat: list, k: int) -> list:
        result = list(range(len(mat)))
        strength_count = {}

        for i in range(len(mat)):
            row = mat[i]
            strength = 0
            for c in row:
                strength += c
            strength_count[i] = strength
        result.sort(key=lambda x: strength_count[x])

        return result[:k]


def solution(l1, l2):
    s = Solution()
    return s.kWeakestRows(l1, l2)


def main():
    inp1 = [[1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1]]
    inp2 = 3

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
