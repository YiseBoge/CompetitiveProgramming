import sys


def flip(A, k):
    result = []
    for i in range(k - 1, -1, -1):
        result += [A[i]]

    result += A[k:]
    return result


def pancake_sort(A):
    flips = []
    current = -1

    l = A
    smallest = l[0]
    largest = l[len(l) - 1]

    i = 0
    while i < (len(l)):
        if (current == 1 and l[i] == largest) or (current == -1 and l[i] == smallest):
            l = flip(l, i + 1)
            flips += [i + 1]
            i = 0
            current *= -1
        else:
            i += 1
        print(l)
    return flips


def solution(l1):
    return pancake_sort(l1)


def main():
    inp1 = [3, 2, 4, 1]
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
