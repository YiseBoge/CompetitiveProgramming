def find_word(s, t):
    for i in range(len(t)):
        if (t[:i + 1][::-1] == t[i:2 * i + 1] and t[i:][::-1] in s or
                t[i:][::-1] == t[-2 * (len(t) - i) + 1:i + 1] and t[:i + 1] in s):
            return "YES"
    return "NO"


if __name__ == "__main__":
    inp, results = int(input()), []
    for _ in range(inp):
        inp1, inp2 = input(), input()
        results.append(find_word(inp1, inp2))
    print(*results, sep="\n")
