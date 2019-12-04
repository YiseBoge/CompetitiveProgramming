import sys


def prefix_calculator(tokens: list) -> int:
    operators = ["+", "-", "*", "/"]
    t = tokens

    while len(t) > 1:
        i = 0
        while t[i] not in operators:
            i += 1

        buffer = t[0:i]
        operator = t[i]
        t = t[i + 1:]

        op2 = int(buffer.pop(i - 1))
        op1 = int(buffer.pop(i - 2))

        res = 0
        if operator == "+":
            res = op1 + op2
        elif operator == "-":
            res = op1 - op2
        elif operator == "*":
            res = op1 * op2
        elif operator == "/":
            a = abs(op1) // abs(op2)
            res = -a if op1 < 0 and op2 >= 0 or op2 < 0 and op1 >= 0 else a
        t = buffer + [res] + t
    return t[0]


def solution(inp):
    return prefix_calculator(inp)


def main():
    # inp = sys.stdin.readline().split()
    inp = ["4", "13", "5", "/", "+"]
    sys.stdout.write(str(solution(inp)))


if __name__ == '__main__':
    main()
