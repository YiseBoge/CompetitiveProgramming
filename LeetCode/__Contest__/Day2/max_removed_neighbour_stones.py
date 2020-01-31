class Solution:
    def removeStones(self, stones: list) -> int:
        neighbour_holder = {}
        visited = set()
        moves = 0

        for i in range(len(stones)):
            stone = stones[i]
            neighbours = []
            for e in stones:
                if e != stone and (e[0] == stone[0] or e[1] == stone[1]):
                    neighbours.append(tuple(e))
            neighbour_holder[tuple(stone)] = neighbours

        for item in neighbour_holder:
            if item not in visited:
                moves += self.do_dfs(item, neighbour_holder, visited) - 1

        return moves

    def do_dfs(self, stone, neighbour_holder, visited):
        visited.add(stone)
        count = 1
        for s in neighbour_holder[stone]:
            if s not in visited:
                count += self.do_dfs(s, neighbour_holder, visited)
        return count


def solution(l1):
    s = Solution()
    return s.removeStones(l1)


def main():
    inp1 = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]

    print(solution(inp1))


if __name__ == '__main__':
    main()
