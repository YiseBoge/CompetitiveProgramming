import sys


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_ints = self.parse(a)
        b_ints = self.parse(b)

        int_result = (a_ints[0] * b_ints[0]) - (a_ints[1] * b_ints[1])
        i_result = (a_ints[0] * b_ints[1]) + (a_ints[1] * b_ints[0])

        return str(int_result) + "+" + str(i_result) + "i"

    def parse(self, string):
        items = string.split("+")

        x = int(items[0])
        i = int(items[1][:-1])

        return x, i


def solution(inp1, inp2):
    s = Solution()
    return s.complexNumberMultiply(inp1, inp2)


def main():
    in1 = "0+100i"
    in2 = "1+1i"
    sys.stdout.write(str(solution(in1, in2)))


if __name__ == '__main__':
    main()
