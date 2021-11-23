def create_teams(skills, threshold):
    skills.sort()
    end, result = len(skills), 0
    for i in range(end - 1, -1, -1):
        if skills[i] * (end - i) >= threshold:
            result += 1
            end = i
    return result


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1, inp2 = list(map(int, input().split()))
        inputs = list(map(int, input().split()))
        results.append(create_teams(inputs, inp2))
    print(*results, sep="\n")
