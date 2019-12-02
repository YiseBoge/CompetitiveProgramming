import sys


def valid_anagram(s, t):
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


def solution(l1, l2):
    return valid_anagram(l1, l2)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = "abcdef"
    inp2 = "acbdfe"
    sys.stdout.write(str(solution(inp1, inp2)))


if __name__ == '__main__':
    main()
