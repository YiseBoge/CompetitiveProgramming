def make_palindrome(string):
    result = ["3", f"L 2", f"R 2", f"R {2 * len(string) - 1}"]
    return "\n".join(result)


if __name__ == "__main__":
    inp = input()
    print(make_palindrome(inp))
