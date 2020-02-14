class Solution:
    def maxDistToClosest(self, seats: list) -> int:
        last_one = -1
        max_distance = 0

        i = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                if last_one < 0:
                    max_distance = i
                    last_one = i
                else:
                    diff = i - last_one
                    max_distance = max(max_distance, diff // 2)
                    last_one = i
        max_distance = max(max_distance, i - last_one)
        return max_distance


def solution(l1):
    s = Solution()
    return s.maxDistToClosest(l1)


def main():
    inp1 = [1, 0, 0, 0, 1, 0, 1]

    print(solution(inp1))


if __name__ == '__main__':
    main()
