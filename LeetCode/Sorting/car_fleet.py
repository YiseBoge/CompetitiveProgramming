import sys


def car_fleet(target: int, position, speed) -> int:
    times_left = []
    fleets = 1
    length = len(position)

    if length <= 1:
        return length

    for i in range(length):
        s = speed[i]
        distance_left = target - position[i]
        times_left.append(distance_left / s)

    times_left = __sort_by_another__(position, times_left)
    print(times_left)
    current_max = times_left[-1]

    for j in range(length - 1, -1, -1):
        if times_left[j] > current_max:
            fleets += 1
            current_max = times_left[j]

    return fleets


def __sort_by_another__(list1, list2):
    items = {}
    length = len(list1)
    results = []

    for i in range(length):
        if items.get(list1[i]) is None:
            items[list1[i]] = [list2[i]]
        else:
            items[list1[i]].append(list2[i])
    for j in sorted(list(items)):
        results += items[j]

    return results


def solution(l1, l2, l3):
    return car_fleet(l1, l2, l3)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = 10
    inp2 = [3, 5, 4, 2]
    inp3 = [3, 5, 4, 2]
    sys.stdout.write(str(solution(inp1, inp2, inp3)))


if __name__ == '__main__':
    main()
