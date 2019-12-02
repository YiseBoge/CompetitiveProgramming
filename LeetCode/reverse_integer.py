import sys


def reverse(x: int) -> int:
    maximum = 2 ** 31 - 1
    minimum = -(2 ** 31)

    is_negative = False
    if x < 0:
        is_negative = True
        x *= -1

    power = 0
    result = 0

    while x // (10 ** power) > 0:
        p1 = (10 ** power)
        p2 = (10 ** (power + 1))

        n = (x % p2) // p1
        result *= 10
        result += n
        power += 1

    if is_negative:
        result *= -1
    if result < minimum or result > maximum:
        return 0

    return result


def solution(inp):
    return reverse(inp)


def main():
    inp = sys.stdin.readline().split()
    in1 = inp[0]
    sys.stdout.write(str(solution(int(in1))))


if __name__ == '__main__':
    main()
