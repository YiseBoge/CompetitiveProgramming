def count_subsets(length):
    return int(length * (length + 1) / 2)


def tell(original, keys):
    available_keys = set(keys)
    subsets_count = 0
    start = 0
    length = len(original)

    for i in range(length):
        if original[i] not in available_keys:
            subsets_count += count_subsets(i - start)
            start = i + 1
        elif i == length - 1:
            subsets_count += count_subsets((i + 1) - start)

    return subsets_count


def solution(inp, inp2):
    return tell(inp, inp2)


def main():
    input().split()
    inp2 = input()
    inp3 = input().split()

    print(solution(inp2, inp3))


if __name__ == "__main__":
    main()
