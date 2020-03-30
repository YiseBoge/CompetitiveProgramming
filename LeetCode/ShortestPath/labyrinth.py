def count_reachables(grid, start, left_max, right_max) -> int:
    print(grid)

    queue = []

    result = 0
    for row in grid:
        for c in row:
            result += 1 if c == 1 else 0
    return result


def solution(l1, l2, l3, l4):
    return count_reachables(l1, l2, l3, l4)


def main():
    rows, columns = map(int, input().split())
    start = tuple(map(int, input().split()))
    x, y = map(int, input().split())
    grid = []
    for i in range(rows):
        inp = input()
        r = []
        for el in inp:
            if el == "*":
                r.append(-1)
            else:
                r.append(0)
        grid.append(r)

    print(solution(grid, start, x, y))


if __name__ == '__main__':
    main()
