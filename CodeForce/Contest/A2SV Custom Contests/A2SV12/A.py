def change_names(names):
    older, library = {}, {}
    for old, new in names:
        key = older[old] if old in older else old
        library[key] = new
        older[new] = key
    return f"{len(library)}\n" + "\n".join(f"{old} {new}" for old, new in library.items())


if __name__ == "__main__":
    inp = int(input())
    inputs = [input().split() for _ in range(inp)]
    print(change_names(inputs))
