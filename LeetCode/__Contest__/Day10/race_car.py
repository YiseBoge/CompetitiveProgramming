import collections


class Solution:
    def racecar(self, target: int) -> int:
        start = (0, 1)
        steps = {start: 0}
        queue = collections.deque([start])
        while queue:
            current = queue.popleft()
            position = current[0]
            speed = current[1]

            if position == target:
                return steps[current]

            nexts = [
                [speed * 2, position + speed],
                [-speed // abs(speed), position]
            ]

            for n in nexts:
                new_state = (n[1], n[0])
                if new_state not in steps:
                    steps[new_state] = steps[current] + 1
                    queue.append(new_state)


def solution(l1):
    s = Solution()
    return s.racecar(l1)


def main():
    inp1 = 10

    print(solution(inp1))


if __name__ == '__main__':
    main()
