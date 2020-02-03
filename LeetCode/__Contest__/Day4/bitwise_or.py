class Solution:
    def subarrayBitwiseORs(self, A: list) -> int:
        result = set()
        prev = set()

        for el in A:
            new = {el}
            for p in prev:
                new.add(p | el)
            for n in new:
                result.add(n)
            prev = new

        return len(result)


def solution(l1):
    s = Solution()
    return s.subarrayBitwiseORs(l1)


def main():
    inp1 = [6, 2, 4]

    print(solution(inp1))


if __name__ == '__main__':
    main()
