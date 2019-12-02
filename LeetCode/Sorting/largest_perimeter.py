import sys


def largest_perimeter(A):
    largest = 0
    l = sorted(A, reverse=True)

    for i in range(len(l) - 2):
        one = l[i]
        two = l[i + 1]
        three = l[i + 2]
        s = one + two + three

        if one < two + three:
            largest = s
            break

    return largest


def solution(l1):
    return largest_perimeter(l1)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = [3, 5, 4, 2]
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
