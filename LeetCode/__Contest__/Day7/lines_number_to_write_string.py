class Solution:
    def numberOfLines(self, widths: list, S: str) -> list:
        lines = 1
        current_length = 0
        for i in S:
            index = ord(i) - 97
            width = widths[index]
            if current_length + width > 100:
                lines += 1
                current_length = width
            else:
                current_length += width

        return [lines, current_length]


def solution(l1, l2):
    s = Solution()
    return s.numberOfLines(l1, l2)


def main():
    inp1 = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    inp2 = "bbbcccdddaaa"

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
