import sys


class Solution:
    def countPrimes(self, n: int) -> int:
        lst = list(range(2, n + 1))
        length = len(lst) - 1
        primes = []

        for i in range(length):
            if lst[i] is not None and self.checkPrime(lst[i], primes):
                val = lst[i]
                j = (val * val) - 2
                while j < length:
                    lst[j] = None
                    j += val

                primes.append(val)

        return len(primes)

    def checkPrime(self, n, primes):
        if n == 2:
            return True
        for i in primes:
            if n % i == 0:
                return False

            return True


def solution(inp):
    s = Solution()
    return s.checkPerfectNumber(inp)


def main():
    in1 = 100
    sys.stdout.write(str(solution(in1)))


if __name__ == '__main__':
    main()
