from collections import deque


def paint(squares):
    opposite, n = {"R": "B", "B": "R"}, len(squares)
    queue, result = deque(), [""] * n + ["R"]
    for i, square in enumerate(squares):
        if square != "?":
            result[i] = square
            queue.append(i)
    if not queue:
        queue.append(len(result) - 1)

    while queue:
        current = queue.popleft()
        for i in (current - 1, current + 1):
            if 0 <= i < n and result[i] == "":
                result[i] = opposite[result[current]]
                queue.append(i)
    return "".join(result[:-1])


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        input()
        results.append(paint(input()))
    print(*results, sep="\n")
