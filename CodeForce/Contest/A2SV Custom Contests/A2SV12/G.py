import sys

input = sys.stdin.readline


def label_graph(words, k):
    trie = {}
    for word in words:
        node = trie
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]

    def can_do(current, bad_result):
        for key, new in current.items():
            if not can_do(new, bad_result):
                return True
        return False if current else bad_result

    can_win, can_lose = can_do(trie, False), can_do(trie, True)
    if can_win == can_lose:
        return "First" if can_win else "Second"
    if can_lose:
        return "Second"
    return "First" if k % 2 else "Second"


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs = [input().strip() for _ in range(inp1)]
    print(label_graph(inputs, inp2))
