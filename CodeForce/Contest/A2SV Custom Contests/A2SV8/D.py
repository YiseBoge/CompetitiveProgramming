def find_music(description, queries):
    result, prefix, ind = [], [0], 0
    for i, song in enumerate(description):
        count, length = song
        prefix.append(prefix[-1] + count * length)
        while ind < len(queries) and prefix[-2] < queries[ind] <= prefix[-1]:
            result.append(str(i + 1))
            ind += 1
    return "\n".join(result)


if __name__ == "__main__":
    inp1, _ = list(map(int, input().split()))
    inputs1 = []
    for _ in range(inp1):
        inputs1.append(list(map(int, input().split())))
    inputs2 = list(map(int, input().split()))
    print(find_music(inputs1, inputs2))
