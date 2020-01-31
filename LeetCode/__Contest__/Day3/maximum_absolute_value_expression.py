class Solution:
    def maxAbsValExpr(self, arr1: list, arr2: list) -> int:
        lis1, lis2, lis3, lis4 = [], [], [], []
        for i in range(len(arr1)):
            a, b = arr1[i], arr2[i]
            lis1.append(a + b + i)
            lis2.append(a + b - i)
            lis3.append(a - b + i)
            lis4.append(a - b - i)
        ans1 = max(lis1) - min(lis1)
        ans2 = max(lis2) - min(lis2)
        ans3 = max(lis3) - min(lis3)
        ans4 = max(lis4) - min(lis4)
        return max(ans1, ans2, ans3, ans4)


def solution(l1, l2):
    s = Solution()
    return s.maxAbsValExpr(l1, l2)


def main():
    inp1 = [1, -2, -5, 0, 10]
    inp2 = [0, -2, -1, -7, -4]

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
