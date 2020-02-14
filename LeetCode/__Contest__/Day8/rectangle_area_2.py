class Solution:
    def rectangleArea(self, rectangles: list) -> int:
        results = set()
        result = 0
        x_list = set()
        y_list = set()
        for rect in rectangles:
            x_list.add(rect[0])
            y_list.add(rect[1])
            x_list.add(rect[2])
            y_list.add(rect[3])
        x_coordinates = sorted(x_list)
        y_coordinates = sorted(y_list)

        for i in range(1, len(x_coordinates)):
            x1 = x_coordinates[i]
            x0 = x_coordinates[i - 1]
            for j in range(1, len(y_coordinates)):
                y1 = y_coordinates[j]
                y0 = y_coordinates[j - 1]

                for rect in rectangles:
                    if rect[0] <= x0 < x1 <= rect[2] and rect[1] <= y0 < y1 <= rect[3]:
                        cell = (x0, y0, x1, y1)
                        if cell not in results:
                            result = (result + (x1 - x0) * (y1 - y0)) % (10 ** 9 + 7)
                            results.add(cell)

        return result


def solution(l1):
    s = Solution()
    return s.rectangleArea(l1)


def main():
    inp1 = [
        [0, 0, 2, 2],
        [1, 0, 2, 3],
        [1, 0, 3, 1]
    ]

    print(solution(inp1))


if __name__ == '__main__':
    main()
