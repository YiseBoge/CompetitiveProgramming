def factors(x):
    result = []
    i = 1
    while i * i < x:
        if x % i == 0:
            result.append(i)
        i += 1
    return result


def gcd(big, small):
    mod = big % small
    if mod == 0:
        return small
    return gcd(small, mod)


def find_nums(lcm):
    f = factors(lcm)
    biggest = lcm

    for i in f:
        bigger = lcm // i
        if bigger < biggest and gcd(i, bigger) == 1:
            biggest = bigger

    return str(lcm // biggest) + " " + str(biggest)


def solution(inp):
    return find_nums(inp)


def main():
    print(solution(int(input())))


if __name__ == "__main__":
    main()
