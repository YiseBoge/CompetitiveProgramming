import sys


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        negative = "" if numerator >= 0 and denominator >= 0 or numerator < 0 and denominator < 0 else "-"
        numerator = abs(numerator)
        denominator = abs(denominator)

        res, rem = str(numerator // denominator), str(numerator % denominator)
        if rem == "0":
            return res if res == "0" else negative + res
        res += "."

        res = self.find_decimal(rem, str(denominator), res, [])
        return negative + res

    def find_decimal(self, small, big, result, passed_rems):
        numerator = small + "0"
        int_num = int(numerator)
        ind_den = int(big)

        res, rem = str(int_num // ind_den), str(int_num % ind_den)
        if rem == "0":
            return result + res

        if rem in passed_rems:
            ind = len(passed_rems) - passed_rems.index(rem)

            if result[-ind] == res:
                return result[:-ind] + "(" + result[-ind:] + ")"
            if result[-ind + 1] == res:
                return result[:-ind + 1] + "(" + result[-ind + 1:] + ")"

        passed_rems.append(rem)
        return self.find_decimal(rem, big, result + res, passed_rems)


def solution(inp1, inp2):
    s = Solution()
    return s.fractionToDecimal(inp1, inp2)


def main():
    in1 = -22
    in2 = 7
    sys.stdout.write(str(solution(in1, in2)))


if __name__ == '__main__':
    main()
