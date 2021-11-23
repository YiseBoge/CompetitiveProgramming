def jump(array):
    for i in range(len(array) - 1, -1, -1):
        next_ind = i + array[i]
        if next_ind < len(array):
            array[i] += array[next_ind]
    return max(array)


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        input()
        results.append(jump(list(map(int, input().split()))))
    print(*results, sep="\n")
