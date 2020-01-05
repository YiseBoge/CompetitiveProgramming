import sys


class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = False
        if n == 0:
            return 1.0

        if n < 0:
            negative = True
            n = -n
        result = x
        i = 2
        mult = x
        mults = [x]

        while i <= n:
            result *= mult
            if i == n:
                break

            if i + i <= n:
                mult = result
                i += i
                mults.append(mult)
            else:
                for j in range(len(mults) - 1, -1, -1):
                    p = 2 ** j
                    if p + i <= n:
                        mult = mults[j]
                        i += p
                        break

        return result if not negative else 1 / result


def solution(inp1, inp2):
    s = Solution()
    return s.myPow(inp1, inp2)


def main():
    in1 = 2.5
    in2 = 10
    sys.stdout.write(str(solution(in1, in2)))


if __name__ == '__main__':
    main()
