import math


def find_pi(k):
    circumference = 1.0
    side = circumference / k
    theta = 360 / k
    alpha = (180 - theta) / 2
    sin_theta = math.sin(math.radians(theta))
    sin_alpha = math.sin(math.radians(alpha))

    radius = side * (sin_alpha / sin_theta)
    pi = circumference / (2 * radius)
    return pi


def solution(num):
    return find_pi(num)


def main():
    while True:
        inp = input()
        print(solution(int(inp)))


if __name__ == '__main__':
    main()
