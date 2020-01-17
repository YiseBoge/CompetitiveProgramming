class Solution:
    def __init__(self):
        self.neighbour_array = ((0, -1), (-1, 0), (1, 0), (0, 1))
        self.visited = set()

    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        current_color = image[sr][sc]
        image[sr][sc] = newColor

        for neighbour in self.find_neighbours(sr, sc):
            r = neighbour[0]
            c = neighbour[1]
            if neighbour not in self.visited and self.check_range(image, neighbour) and image[r][c] == current_color:
                self.visited.add(neighbour)
                self.floodFill(image, r, c, newColor)

        return image

    def find_neighbours(self, r, c):
        result = []
        for n in self.neighbour_array:
            new_row = r + n[0]
            new_col = c + n[1]
            result.append((new_row, new_col))

        return result

    def check_range(self, image, cell):
        r = cell[0]
        c = cell[1]
        return 0 <= r < len(image) and 0 <= c < len(image[r])


def solution(l1, l2, l3, l4):
    s = Solution()
    return s.floodFill(l1, l2, l3, l4)


def main():
    inp1 = [[1, 1, 1], [1, 4, 0], [1, 0, 5]]
    inp2 = 1
    inp3 = 1
    inp4 = 5

    print(solution(inp1, inp2, inp3, inp4))


if __name__ == '__main__':
    main()
