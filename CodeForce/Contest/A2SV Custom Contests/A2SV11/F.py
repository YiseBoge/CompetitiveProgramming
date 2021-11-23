def pass_exams(exams, difficulty, n, m):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        visited, needed = {0}, 0
        for i in range(mid, -1, -1):
            if exams[i] not in visited:
                needed += difficulty[exams[i] - 1]
                visited.add(exams[i])
            elif needed > 0:
                needed -= 1
        if len(visited) == m + 1 and needed == 0:
            end = mid - 1
        else:
            start = mid + 1
    return start + 1 if start < n else -1


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs1 = list(map(int, input().split()))
    inputs2 = list(map(int, input().split()))
    print(pass_exams(inputs1, inputs2, inp1, inp2))
