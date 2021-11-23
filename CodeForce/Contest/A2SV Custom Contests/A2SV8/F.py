def find_word(words, queries):
    result = []
    root = [None] * 4
    for word in words:
        node = root
        for w in word:
            ind = ord(w) - ord("a")
            if not node[ind]:
                node[ind] = [None] * 4
            node = node[ind]
        node[-1] = True

    def traverse(current, changed, string, start):
        for j in range(start, len(string)):
            index = ord(string[j]) - ord("a")
            if not changed:
                for i in range(3):
                    if current[i] and i != index and traverse(current[i], True, string, j + 1):
                        return True
            if not current[index]:
                return False
            current = current[index]
        return changed and current[-1]

    for word in queries:
        result.append("YES" if traverse(root, False, word, 0) else "NO")
    return "\n".join(result)


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs1, inputs2 = [], []
    for _ in range(inp1):
        inputs1.append(input())
    for _ in range(inp2):
        inputs2.append(input())
    print(find_word(inputs1, inputs2))
