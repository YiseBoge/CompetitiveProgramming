class Solution:
    def findLongestChain(self, pairs: list) -> int:
        sorted_pairs = sorted(pairs)
        chain_count = {}
        result = 0
        for i in range(len(sorted_pairs)):
            result = max(result, self.count_pairs(sorted_pairs, i, chain_count))
        return result

    def count_pairs(self, pairs, current, chain_count):
        if current in chain_count:
            return chain_count[current]
        val = pairs[current]
        result = 0

        for i in range(current, len(pairs)):
            nxt = pairs[i]
            if val[1] < nxt[0]:
                result = max(result, self.count_pairs(pairs, i, chain_count))
        result += 1

        chain_count[current] = result
        return result


def solution(l1):
    s = Solution()
    return s.findLongestChain(l1)


def main():
    inp1 = [
        [0, 1],
        [5, 6],
        [2, 4]
    ]

    print(solution(inp1))


if __name__ == '__main__':
    main()
