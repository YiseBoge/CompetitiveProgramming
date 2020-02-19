class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        counts = {}
        specials = {"!", "?", "'", ",", ";", ".", " "}
        banned_words = set(banned)

        buffer = []
        for x in range(len(paragraph)):
            i = paragraph[x]
            if i in specials:
                s = "".join(buffer).lower()
                if len(s) > 0 and s not in banned_words:
                    if s in counts:
                        counts[s] += 1
                    else:
                        counts[s] = 1
                buffer = []
            elif x == len(paragraph) - 1:
                buffer.append(i)
                s = "".join(buffer).lower()
                if len(s) > 0 and s not in banned_words:
                    if s in counts:
                        counts[s] += 1
                    else:
                        counts[s] = 1
                buffer = []
            else:
                buffer.append(i)

        result = list(counts.keys())[0]
        for i in counts:
            if counts[i] > counts[result]:
                result = i

        return result


def solution(l1, l2):
    s = Solution()
    return s.mostCommonWord(l1, l2)


def main():
    inp1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    inp2 = ["hit"]

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
