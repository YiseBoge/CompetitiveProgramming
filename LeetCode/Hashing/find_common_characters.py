import sys


class Solution:
    def commonChars(self, A):
        old = {}
        new = {}
        result = []

        first = A[0]
        for f in first:
            old[f] = 1 if not old.get(f) else old[f] + 1

        for i in range(1, len(A)):
            for c in A[i]:
                if old.get(c):
                    if not new.get(c):
                        new[c] = 1
                    elif new.get(c) < old.get(c):
                        new[c] += 1

            old = new
            new = {}

        for l in old:
            result += [l] * old[l]
        return result


def solution(l1):
    s = Solution()
    return s.commonChars(l1)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()

    inp1 = ["bella", "label", "roller"]
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
