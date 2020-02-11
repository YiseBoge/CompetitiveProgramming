class Solution:
    def uniqueMorseRepresentations(self, words: list) -> int:
        translations = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                        "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        results = set()
        for word in words:
            res = ""
            for c in word:
                index = ord(c) - 97
                res += translations[index]
            results.add(res)

        return len(results)


def solution(l1):
    s = Solution()
    return s.uniqueMorseRepresentations(l1)


def main():
    inp1 = ["gin", "zen", "gig", "msg"]

    print(solution(inp1))


if __name__ == '__main__':
    main()
