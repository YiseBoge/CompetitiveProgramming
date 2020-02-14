class Solution:
    def loudAndRich(self, richer: list, quiet: list) -> list:
        rich_friends = {}
        for i in range(len(quiet)):
            rich_friends[i] = []
        for i in richer:
            rich_friends[i[1]].append(i[0])

        result = list(range(len(quiet)))
        for i in range(len(quiet)):
            self.find_noisy(quiet, rich_friends, i, i, result, set())

        return result

    def find_noisy(self, quiet, rich_friends, index, current, result, visited):
        if quiet[current] < quiet[result[index]]:
            result[index] = current

        visited.add(current)
        for el in rich_friends[current]:
            if el not in visited:
                self.find_noisy(quiet, rich_friends, index, el, result, visited)


def solution(l1, l2):
    s = Solution()
    return s.loudAndRich(l1, l2)


def main():
    inp1 = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    inp2 = [3, 2, 5, 4, 6, 1, 7, 0]

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
