from heapq import heapify, heappop, heappush


def find_temperatures(position, temperature, n):
    result = [""] * n
    queue = []
    for p, t in zip(position, temperature):
        queue.append((t, p - 1))
    heapify(queue)
    while queue:
        temp, ind = heappop(queue)
        if result[ind] == "":
            result[ind] = str(temp)
            for i in (ind - 1, ind + 1):
                if 0 <= i < n and result[i] == "":
                    heappush(queue, (temp + 1, i))
    return " ".join(result)


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        input()
        inp1, _ = list(map(int, input().split()))
        inputs1 = list(map(int, input().split()))
        inputs2 = list(map(int, input().split()))
        results.append(find_temperatures(inputs1, inputs2, inp1))
    print(*results, sep="\n")
