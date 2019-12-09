import sys


def k_closest(points, K) -> list:
    collected_items = {}
    result = []

    for i in points:
        d = i[0] ** 2 + i[1] ** 2
        if collected_items.get(d) is None:
            collected_items[d] = [i]
        else:
            collected_items[d] += [i]

    distances = sorted(collected_items.keys())

    j = 0
    for m in distances:
        if j >= K:
            break
        result += collected_items[m]
        j += len(collected_items[m])

    return result


def solution(l1, l2):
    return k_closest(l1, l2)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = [[1, 3], [-2, 2]]
    inp2 = 1
    sys.stdout.write(str(solution(inp1, inp2)))


if __name__ == '__main__':
    main()
