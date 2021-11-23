from collections import defaultdict


def process(queries):
    nums, result = defaultdict(int), []
    for action, val in queries:
        mods = [str(int(v) % 2) for v in val[::-1]]
        val = "".join(reversed(mods)).zfill(18)
        if action == "-":
            nums[val] -= 1
        elif action == "+":
            nums[val] += 1
        else:
            result.append(str(nums[val]))
    return "\n".join(result)


if __name__ == "__main__":
    inp = int(input())
    inputs = [input().split() for _ in range(inp)]
    print(process(inputs))
