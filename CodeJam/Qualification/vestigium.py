def make_keyboard(matrix):
    trace, r, c = 0, 0, 0
    rows = [set() for _ in range(len(matrix))]
    cols = [set() for _ in range(len(matrix))]
    found_rows, found_cols = set(), set()

    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if i == j:
                trace += num

            if i not in found_rows and num in rows[i]:
                found_rows.add(i)
                r += 1

            if j not in found_cols and num in cols[j]:
                found_cols.add(j)
                c += 1
            rows[i].add(num)
            cols[j].add(num)

    return trace, r, c


def solution(inp1):
    return make_keyboard(inp1)


def main():
    length = int(input())

    for i in range(length):
        matrix = []
        size = int(input())
        for _ in range(size):
            inp = list(map(int, input().split()))
            matrix.append(inp)
        result = solution(matrix)
        print("Case #" + str(i + 1) + ":", result[0], result[1], result[2])


if __name__ == "__main__":
    main()
