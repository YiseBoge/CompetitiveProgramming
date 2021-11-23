import sys
from collections import defaultdict

input = sys.stdin.readline


def change_name(name, bonuses, k):
    memory, n = defaultdict(int), len(name)
    bonus, options = defaultdict(int), set()
    for one, two, val in bonuses:
        bonus[(one, two)] = int(val)
        options.add(one)
        options.add(two)

    for i in range(26):
        c = chr(ord("a") + i)
        if c not in options:
            options.add(c)
            break

    for ind in range(len(name) - 1, -1, -1):
        last_options = options | {name[ind - 1]} if ind > 0 else {"#"}
        for last in last_options:
            for rem in range(k + 1):
                state = f"{ind},{last},{rem}"
                new_options = options | {name[ind]} if rem > 0 else {name[ind]}
                for curr in new_options:
                    new_state = f"{ind + 1},{curr},{rem - (curr != name[ind])}"
                    memory[state] = max(memory[state], memory[new_state] + bonus[(last, curr)])
    return memory[f"0,#,{k}"]


if __name__ == "__main__":
    inp1, inp2 = input().split()
    inputs = []
    for _ in range(int(input())):
        inputs.append(input().split())
    print(change_name(inp1, inputs, int(inp2)))
