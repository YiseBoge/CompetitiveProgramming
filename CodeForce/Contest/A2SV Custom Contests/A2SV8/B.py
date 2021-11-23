from collections import defaultdict


def find_popularity(reposts):
    graph = defaultdict(list)
    for copier, poster in reposts:
        graph[poster.lower()].append(copier.lower())

    def traverse(person):
        nonlocal graph
        return max([traverse(other) + 1 for other in graph[person]] + [1])

    return traverse("polycarp")


if __name__ == "__main__":
    inp = int(input())
    inputs = []
    for _ in range(inp):
        inputs.append(input().split(" reposted "))
    print(find_popularity(inputs))
