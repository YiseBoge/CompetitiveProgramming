class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.find_palindrome(s, 0, len(s) - 1, {})

    def find_palindrome(self, string, start, end, registered):
        current = (start, end)
        if current in registered:
            return registered[current]
        if start == end:
            return 1
        if start > end:
            return 0

        if string[start] != string[end]:
            result1 = self.find_palindrome(string, start, end - 1, registered)
            result2 = self.find_palindrome(string, start + 1, end, registered)
            result = max(result1, result2)
        else:
            result = 2 + self.find_palindrome(string, start + 1, end - 1, registered)

        registered[current] = result
        return result


def solution(l1):
    s = Solution()
    return s.longestPalindromeSubseq(l1)


def main():
    inp1 = "palindrome"

    print(solution(inp1))


if __name__ == '__main__':
    main()
