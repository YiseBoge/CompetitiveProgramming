import collections


class Solution:
    def splitArraySameAverage(self, A: list) -> bool:
        ends = set()
        biggest_end = 0
        total_length, total_sum = len(A), sum(A)

        for i in range(1, len(A) // 2 + 1):
            if (i * total_sum) % total_length == 0:
                new = (i * total_sum) // total_length
                ends.add((new, i))
                ends.add((total_sum - new, total_length - i))
                biggest_end = max(biggest_end, i)

        start = (0, 0)
        visited = {}
        queue = collections.deque([start])
        visited[start] = 0
        while queue:
            state = queue.popleft()
            curr_items = set()
            if state in ends:
                return True

            for i in range(total_length):
                val = A[i]
                if (visited[state] >> i) % 2 == 1:
                    continue
                new_state = (state[0] + val, state[1] + 1)
                if new_state in curr_items:
                    continue
                curr_items.add(new_state)
                if new_state in visited or new_state[1] > biggest_end:
                    continue
                queue.append(new_state)
                visited[new_state] = visited[state] + 2 ** i

        return False


def solution(l1):
    s = Solution()
    return s.splitArraySameAverage(l1)


def main():
    inp1 = [1, 2, 3, 4, 5, 6, 7, 8]

    print(solution(inp1))


if __name__ == '__main__':
    main()
