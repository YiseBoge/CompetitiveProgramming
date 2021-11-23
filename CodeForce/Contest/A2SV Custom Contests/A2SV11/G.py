import sys

input = sys.stdin.readline


def sleep_well(hours, n, h, l, r):
    memory = [[0] * h for _ in range(n + 1)]
    for ind in range(n - 1, -1, -1):
        for time in range(h):
            for addable in (hours[ind], hours[ind] - 1):
                new_time = (time + addable) % h
                res = l <= new_time <= r
                memory[ind][time] = max(memory[ind][time], memory[ind + 1][new_time] + res)
    return memory[0][0]


if __name__ == "__main__":
    inp = list(map(int, input().split()))
    inputs = list(map(int, input().split()))
    print(sleep_well(inputs, *inp))
