def check_anagram(s, t):
    counting = {}
    for i in s:
        if i not in counting.keys():
            counting[i] = 1
        else:
            counting[i] += 1

    for j in t:
        if j not in counting.keys():
            return False
        else:
            counting[j] -= 1

    for k in counting.keys():
        if counting[k] > 0:
            return False

    return True


def check_hash(word, hashed):
    correct = "YES"
    incorrect = "NO"

    small_length = len(word)
    big_length = len(hashed)

    for i in range((big_length - small_length) + 1):
        end = i + small_length
        string = hashed[i: end]
        if check_anagram(word, string):
            return correct

    return incorrect


def solution(inp1, inp2):
    return check_hash(inp1, inp2)


def main():
    inp1 = input()
    length = int(inp1)

    result = []
    for i in range(length):
        inp2 = input()
        inp3 = input()
        result += [solution(inp2, inp3)]

    print(*result, sep="\n")


if __name__ == "__main__":
    main()
