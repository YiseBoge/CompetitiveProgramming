class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        smallest = S
        if K == 1:
            for i in range(len(S)):
                new = S[i:] + S[:i]
                smallest = min(smallest, new)
            return smallest

        return "".join(sorted(S))


def solution(l1, l2):
    s = Solution()
    return s.orderlyQueue(l1, l2)


def main():
    inp1 = "abdfgaefas"
    inp2 = 1

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
