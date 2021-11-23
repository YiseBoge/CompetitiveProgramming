import heapq


def digits(num):
    queue, visited = [(0, num)], set()
    while queue:
        current, count = heapq.heappop(queue)
        if current == 0:
            return count
        options = ["1" * len(abs(num))]
        options.append(options[-1][1:] if int(options[-1]) > int(num) else options[-1] + "1")
        small, big = tuple(sorted(options))
        if small not in visited:
            visited.add(small)
            heapq.heappush(queue, (count + len(small), current - small))
        if big not in visited:
            visited.add(big)
            heapq.heappush(queue, (count + len(big), big - current))
    return num


if __name__ == "__main__":
    print(digits(input()))
