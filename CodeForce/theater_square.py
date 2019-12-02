import sys


def solution(in1, in2, in3):
    h = in1 // in3
    h += 1 if in1 % in3 > 0 else 0
    v = in2 // in3
    v += 1 if in2 % in3 > 0 else 0
    return h * v


def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    inp = sys.stdin.readline().split()

    in1 = int(inp[0])
    in2 = int(inp[1])
    in3 = int(inp[2])

    sys.stdout.write(str(solution(in1, in2, in3)))


if __name__ == "__main__":
    main()
