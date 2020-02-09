class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        pushed, result = 0, 0
        for i in S:
            if i == "(":
                pushed += 1
            elif i == ")":
                if pushed == 0:
                    result += 1
                else:
                    pushed -= 1
        return result + pushed


def solution(l1):
    s = Solution()
    return s.minAddToMakeValid(l1)


def main():
    inp1 = "()))(("

    print(solution(inp1))


if __name__ == '__main__':
    main()
