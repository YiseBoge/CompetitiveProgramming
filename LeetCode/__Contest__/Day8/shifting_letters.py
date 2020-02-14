class Solution:
    def shiftingLetters(self, S: str, shifts: list) -> str:
        work = list(S)
        total = sum(shifts)

        for i in range(len(shifts)):
            index = ord(work[i]) - ord("a")
            new_ind = (index + total) % 26
            work[i] = chr(ord("a") + new_ind)
            total -= shifts[i]

        return "".join(work)


def solution(l1, l2):
    s = Solution()
    return s.shiftingLetters(l1, l2)


def main():
    inp1 = "bbbcccdddaaa"
    inp2 = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
