import sys


def right_angle(num):
    for i in range(num):
        for j in range(i + 1):
            print("*", end=" ")
        print()


def pointy(num):
    for i in range(num):
        print(" " * (num - i), end="")
        for j in range(i + 1):
            print("*", end=" ")
        print()


def solution(num):
    # right_angle(num)
    pointy(num)
    return "Done"


def main():
    inp = sys.stdin.readline().split()
    in1 = inp[0]
    sys.stdout.write(str(solution(int(in1))))


if __name__ == '__main__':
    main()
