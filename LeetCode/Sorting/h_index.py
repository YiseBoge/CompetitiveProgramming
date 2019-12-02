import sys


def h_index(citations) -> int:
    l = sorted(citations, reverse=True)

    i = 0
    while i < len(l):
        if i >= l[i]:
            return i
        i += 1

    return i


def solution(l1):
    return h_index(l1)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = [3]
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
