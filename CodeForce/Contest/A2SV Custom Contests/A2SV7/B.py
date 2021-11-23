def can_win(alice, bob, target, n):
    quadrants = [lambda curr, bad: curr[0] < bad[0] and curr[1] < bad[1],
                 lambda curr, bad: curr[0] > bad[0] and curr[1] < bad[1],
                 lambda curr, bad: curr[0] > bad[0] and curr[1] > bad[1],
                 lambda curr, bad: curr[0] < bad[0] and curr[1] > bad[1]]
    results = []
    for node in [bob, target]:
        for i, check in enumerate(quadrants):
            if check(node, alice):
                results.append(i)
                break
    return "YES" if results[0] == results[1] else "NO"


if __name__ == "__main__":
    inp = int(input())
    inp1 = tuple(map(int, input().split()))
    inp2 = tuple(map(int, input().split()))
    inp3 = tuple(map(int, input().split()))
    print(can_win(inp1, inp2, inp3, inp))
