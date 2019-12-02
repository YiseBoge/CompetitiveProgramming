import sys


def sort_by_distance(R: int, C: int, r0: int, c0: int):
    collected_items = {}
    origin = [r0, c0]
    result = []

    for i in range(R):
        for j in range(C):
            k = [i, j]
            d = abs(k[0] - origin[0]) + abs(k[1] - origin[1])

            if collected_items.get(d) is None:
                collected_items[d] = [k]
            else:
                collected_items[d] += [k]

    distances = sorted(collected_items.keys())

    for m in distances:
        result += collected_items[m]

    return result


def solution(l1, l2, l3, l4):
    return sort_by_distance(l1, l2, l3, l4)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = 89
    inp2 = 90
    inp3 = 21
    inp4 = 65
    sys.stdout.write(str(solution(inp1, inp2, inp3, inp4)))


if __name__ == '__main__':
    main()
