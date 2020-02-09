class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        small = 0
        for i in t:
            if small >= len(s):
                break
            if i == s[small]:
                small += 1
        return small == len(s)


def solution(l1, l2):
    s = Solution()
    return s.isSubsequence(l1, l2)


def main():
    inp1 = "abc"
    inp2 = "abracadabra"

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
