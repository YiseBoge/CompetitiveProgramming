def remove_letters(string):
    removed, count = True, 0
    while removed:
        removed = False
        best, items = chr(1), {}
        for i, c in enumerate(string):
            if i > 0 and ord(c) == ord(string[i - 1]) + 1 or i < len(string) - 1 and ord(c) == ord(string[i + 1]) + 1:
                if string[i] > best:
                    best, items = string[i], {i}
                elif string[i] == best:
                    items.add(i)
        if items:
            removed, count = True, count + len(items)
            string = "".join(c for i, c in enumerate(string) if i not in items)
    return count


if __name__ == "__main__":
    _, inp1 = input(), input()
    print(remove_letters(inp1))
