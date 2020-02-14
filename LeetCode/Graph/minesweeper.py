import collections


class Solution:
    def updateBoard(self, board: list, click: list) -> list:
        neighbours = [
            (1, 0), (0, 1), (-1, 0), (0, -1),
            (1, 1), (-1, -1), (-1, 1), (1, -1)
        ]
        queue = collections.deque([tuple(click)])
        visited = {tuple(click)}

        while queue:
            current = queue.popleft()
            if board[current[0]][current[1]] == "M":
                board[current[0]][current[1]] = "X"
                break

            mines_around = 0
            for n in neighbours:
                new_i = current[0] + n[0]
                new_j = current[1] + n[1]

                if (0 <= new_i < len(board) and
                        0 <= new_j < len(board[0]) and
                        (new_i, new_j) not in visited):
                    if board[new_i][new_j] == "M":
                        mines_around += 1

            if mines_around > 0:
                board[current[0]][current[1]] = str(mines_around)
                continue
            else:
                for n in neighbours:
                    new_i = current[0] + n[0]
                    new_j = current[1] + n[1]

                    if (0 <= new_i < len(board) and
                            0 <= new_j < len(board[0]) and
                            (new_i, new_j) not in visited):
                        if board[new_i][new_j] != "M":
                            queue.append((new_i, new_j))
                            visited.add((new_i, new_j))

            board[current[0]][current[1]] = "B"

        return board


def solution(l1, l2):
    s = Solution()
    return s.updateBoard(l1, l2)


def main():
    inp1 = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"]
    ]
    inp = [3, 0]

    print(solution(inp1, inp))


if __name__ == '__main__':
    main()
