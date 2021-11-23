def erase(num):
    result = ["2"]
    if num == 2:
        result.append("1 2")
    else:
        result.append(f"{num - 2} {num}")
        result.append(f"{num - 1} {num - 1}")
    for i in range(num - 3, 0, -1):
        result.append(f"{i} {i + 2}")
    return "\n".join(result)


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        results.append(erase(int(input())))
    print(*results, sep="\n")
