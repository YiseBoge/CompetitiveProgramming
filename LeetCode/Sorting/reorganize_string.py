import sys


def __max(L, ex):
    m = ""
    for i in L.keys():
        if i is not ex and L[i] > 0:
            if L.get(m) is None or (i is not ex and L[i] > 0 and L[i] > L[m]):
                m = i

    return m


def reorganize_string(S) -> str:
    collected_chars = {}
    result = ""
    length = len(S)

    for i in S:
        if collected_chars.get(i) is None:
            collected_chars[i] = 1
        else:
            collected_chars[i] += 1

    m = None
    for k in range(length):
        m = __max(collected_chars, m)
        if m == '':
            return ''
        result += m
        collected_chars[m] -= 1

    return result


def solution(l1):
    return reorganize_string(l1)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = "apples"
    sys.stdout.write(str(solution(inp1)))


if __name__ == '__main__':
    main()
