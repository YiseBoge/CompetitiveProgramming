class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        result = []
        string = s

        while True:
            go_again = False
            i = 0

            while i < len(string):
                buffer = []

                for j in range(k):
                    if i + j >= len(string):
                        break
                    if len(buffer) < 1 or string[i + j] == buffer[-1]:
                        buffer.append(string[i + j])
                    else:
                        break

                if len(buffer) == k:
                    go_again = True
                else:
                    result += buffer
                i += len(buffer)

            string = ''.join(result)
            result = []

            if not go_again:
                break

        return string


def solution(l1, l2):
    s = Solution()
    return s.removeDuplicates(l1, l2)


def main():
    inp1 = "pbbcggttciiippooaais"
    inp2 = 2

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
