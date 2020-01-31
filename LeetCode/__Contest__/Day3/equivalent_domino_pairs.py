class Solution:
    def numEquivDominoPairs(self, dominoes: list) -> int:
        equivalent_count = 0
        count_holder = {}

        for domino in dominoes:
            dom = (domino[0], domino[1])
            rev = (domino[1], domino[0])

            if count_holder.get(dom):
                count_holder[dom][1] += count_holder[dom][0]
                count_holder[dom][0] += 1
            elif count_holder.get(rev):
                count_holder[rev][1] += count_holder[rev][0]
                count_holder[rev][0] += 1
            else:
                count_holder[dom] = [1, 0]

        for d in count_holder:
            equivalent_count += count_holder[d][1]

        return equivalent_count


def solution(l1):
    s = Solution()
    return s.numEquivDominoPairs(l1)


def main():
    inp1 = [[1, 2], [2, 1], [3, 4], [5, 6]]

    print(solution(inp1))


if __name__ == '__main__':
    main()
