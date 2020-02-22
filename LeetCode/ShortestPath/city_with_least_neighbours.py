class Solution:
    def findTheCity(self, n: int, edges: list, distanceThreshold: int) -> int:
        res = []
        for i in range(n):
            res.append([10001] * n)

        for e in edges:
            res[e[0]][e[1]] = res[e[1]][e[0]] = e[2]

        for k in range(n):
            for i in range(n):
                for j in range(i + 1, n):
                    r1, r2 = res[i][k], res[k][j]
                    prev = res[i][j]
                    res[j][i] = res[i][j] = min(prev, r1 + r2)

        result = n - 1
        neighbours_count = n - 1
        for i in range(n):
            row = res[i]
            count = 0
            for n in row:
                if n <= distanceThreshold:
                    count += 1
            if count <= neighbours_count:
                result = i
                neighbours_count = count

        return result


def solution(l1, l2, l3):
    s = Solution()
    return s.findTheCity(l1, l2, l3)


def main():
    inp1 = 5
    inp2 = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    inp3 = 5
    print(solution(inp1, inp2, inp3))


if __name__ == '__main__':
    main()
