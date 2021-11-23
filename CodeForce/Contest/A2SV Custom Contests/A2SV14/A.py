def make_palindrome(string, a, b):
    counts, n = {"0": a, "1": b}, len(string)
    for i in range(n):
        if string[i] != "?":
            if string[n - i - 1] == "?":
                string[n - i - 1] = string[i]
            elif string[i] != string[n - i - 1]:
                return -1
            counts[string[i]] -= 1
        elif string[n - i - 1] != "?":
            counts[string[n - i - 1]] -= 1

    current = "0"
    if counts[current] % 2 and n % 2 and string[n // 2] == "?":
        string[n // 2] = current
        counts[current] -= 1

    for i in range((n + 1) // 2):
        if string[i] == "?":
            while counts[current] <= 0:
                if current == "1":
                    return -1
                current = "1"

            string[i] = string[n - i - 1] = current
            counts[current] -= 1 + (i < n - i - 1)
    return "".join(string) if counts["0"] == counts["1"] == 0 else -1


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1, inp2 = list(map(int, input().split()))
        inputs = list(input())
        results.append(make_palindrome(inputs, inp1, inp2))
    print(*results, sep="\n")
