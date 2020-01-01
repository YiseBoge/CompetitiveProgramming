import sys


class Solution:
    def fractionAddition(self, expression: str) -> str:
        parsed = self.parse(expression)
        nums = parsed[0]
        denoms = parsed[1]

        common_denominator = denoms[0]
        for i in denoms:
            common_denominator *= i

        common_numerator = 0
        for j in range(len(nums)):
            factor = common_denominator // denoms[j]
            common_numerator += nums[j] * factor

        div = self.gcd(common_numerator, common_denominator)
        return str(common_numerator // div) + "/" + str(common_denominator // div)

    def gcd(self, big, small):
        mod = big % small
        if mod == 0:
            return small
        return self.gcd(small, mod)

    def parse(self, nums):
        fractions = []
        numerators = []
        denominators = []
        plussed = nums.split("+")

        for i in plussed:
            minuses = ("-" + i).split("-")
            for j in range(len(minuses)):
                if minuses[j] == "":
                    minuses[j + 1] = "-" + minuses[j + 1]
                elif minuses[j] != "-":
                    a = minuses[j][1:] if minuses[j][0] == "-" else "-" + minuses[j]
                    fractions.append(a)

        for fraction in fractions:
            f = fraction.split("/")
            numerators.append(int(f[0]))
            denominators.append(int(f[1]))
        return numerators, denominators


def solution(inp1):
    s = Solution()
    return s.fractionAddition(inp1)


def main():
    in1 = "-1/3-1/3-1/3-1/3-1/3-1/3-1/3-1/3-1/3-1/3"
    sys.stdout.write(str(solution(in1)))


if __name__ == '__main__':
    main()
