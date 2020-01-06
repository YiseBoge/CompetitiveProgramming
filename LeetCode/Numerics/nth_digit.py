import sys


class Solution:
    def findNthDigit(self, n: int) -> int:
        return self.digitFinder(-1, 1, n)

    def digitFinder(self, last_max, power, remaining):
        next_max = 10 ** power - 1
        numbers_count = next_max - last_max
        digits_count = numbers_count * power

        if digits_count < remaining:
            return self.digitFinder(next_max, power + 1, remaining - digits_count)

        current_offset = remaining // power
        current_digit = remaining % power

        number = last_max + current_offset + 1
        result = int(str(number)[current_digit])
        return result


def solution(inp):
    s = Solution()
    return s.findNthDigit(inp)


def main():
    in1 = 11
    sys.stdout.write(str(solution(in1)))


if __name__ == '__main__':
    main()
