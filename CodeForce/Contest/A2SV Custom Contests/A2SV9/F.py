def kill(bosses):
    result = count = 0
    for num in bosses[1:]:
        if num == "0":
            result += count // 3
            count = 0
        else:
            count += 1
    result += count // 3
    return result + (bosses[0] == "1")


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        input()
        results.append(kill(input().split()))
    print(*results, sep="\n")
