import sys


def is_valid(s: str) -> bool:
    brackets = {')': '(', '}': '{', ']': '['}
    queue = []

    for i in s:
        if i in brackets.keys():
            if len(queue) == 0:
                return False
            a = queue.pop()
            if a != brackets[i]:
                return False
        else:
            queue += [i]

    return True if len(queue) == 0 else False


def solution(inp):
    return is_valid(inp)


def main():
    # inp = sys.stdin.readline().split()
    inp = "()"
    sys.stdout.write(str(solution(inp)))


if __name__ == '__main__':
    main()
