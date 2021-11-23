state = []


def get_height(width, height):
    global state
    widest, highest = state[-1]
    while state and state[-1][0] <= width:
        _, h = state.pop()
        highest = h
    while state and highest + height >= state[-1][1]:
        w, _ = state.pop()
        widest = w
    state.append((widest, highest + height))
    return highest


def solution(inp1, inp2):
    return get_height(inp1, inp2)


def main():
    global state
    _ = int(input())
    for i, s in enumerate(input().split()):
        state.append((i + 1, int(s)))
    state.reverse()

    result = []
    for _ in range(int(input())):
        inp1, inp2 = input().split()
        result.append(solution(int(inp1), int(inp2)))
    print(*result, sep="\n")


if __name__ == "__main__":
    main()
