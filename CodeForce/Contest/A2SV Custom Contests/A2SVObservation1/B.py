def counter_example(size):
    return "2 " * (size - 1) + "1" if size > 2 else "-1"


if __name__ == "__main__":
    inp = int(input())
    print(counter_example(inp))
