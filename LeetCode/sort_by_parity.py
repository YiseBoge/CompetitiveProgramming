import sys


def sort_by_parity(A):
    evens = []
    odds = []

    for j in A:
        if j % 2 == 0:
            evens += [j]
        else:
            odds += [j]

    i1 = 0
    i2 = 0
    result = []

    for i in range(len(A)):
        if i % 2 == 0:
            result += evens[i1: i1 + 1]
            i1 += 1
        else:
            result += odds[i2: i2 + 1]
            i2 += 1

    return result


def solution(l1):
    return sort_by_parity(l1)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = [3, 5, 4, 2]
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
