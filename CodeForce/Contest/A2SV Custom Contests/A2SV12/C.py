import sys

input = sys.stdin.readline


def make_supervisor(qualifications, requests, n):
    manager = [float('inf')] * n
    for supervisor, subordinate, cost in requests:
        manager[subordinate - 1] = min(manager[subordinate - 1], cost)
    assigned = [cost for cost in manager if cost < float('inf')]
    return sum(assigned) if len(assigned) == n - 1 else -1


if __name__ == "__main__":
    inp1 = int(input())
    inputs1 = list(map(int, input().split()))
    inp2 = int(input())
    inputs2 = [list(map(int, input().split())) for _ in range(inp2)]
    print(make_supervisor(inputs1, inputs2, inp1))
