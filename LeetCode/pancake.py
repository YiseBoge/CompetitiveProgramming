import sys


def flip(A, k):
    result = []
    for i in range(k - 1, -1, -1):
        result += [A[i]]

    result += A[k:]
    return result


def pancake_sort(A):
    flips = []
    maximum = len(A)
    largest = max(A)

    while maximum > 0:
        for i in range(maximum):
            if A[i] == largest:
                A = flip(A, i + 1)
                A = flip(A, maximum)
                flips += [i + 1, maximum]
                maximum -= 1
                largest = max(A[0:maximum]) if maximum > 0 else 0
                break
    return flips


def solution(l1):
    return pancake_sort(l1)


def main():
    inp1 = [3, 2, 4, 1]
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
