import collections


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: list, blue_edges: list) -> list:
        graph_holder = {}

        for color in range(2):
            for item in [red_edges, blue_edges][color]:
                start = item[0]
                end = item[1]
                if graph_holder.get(start) and end not in graph_holder[start][color]:
                    graph_holder[start][color].append(end)
                elif color == 0:
                    graph_holder[start] = [[end], []]
                elif color == 1:
                    graph_holder[start] = [[], [end]]

        for i in range(n):
            if i not in graph_holder:
                graph_holder[i] = [[], []]
        result = [-1] * n
        visited = set()

        state1 = (0, 0)
        state2 = (0, 1)
        queue = collections.deque([state1, state2])
        visited.add(state1)
        visited.add(state2)

        distances = {state1: 0, state2: 0}

        while queue:
            current = queue.popleft()
            current_node, color = current
            distance = distances[current]

            result[current_node] = distance if result[current_node] == -1 or distance < result[current_node] else \
                result[current_node]

            for neighbour in graph_holder[current_node][color]:
                new_state = (neighbour, (color + 1) % 2)
                if new_state not in visited:
                    distances[new_state] = distance + 1
                    queue.append(new_state)
                    visited.add(new_state)

        return result


def solution(l1, l2, l3):
    s = Solution()
    return s.shortestAlternatingPaths(l1, l2, l3)


def main():
    inp1 = 3
    inp2 = [[0, 1], [0, 2]]
    inp3 = [[1, 0]]

    print(solution(inp1, inp2, inp3))


if __name__ == '__main__':
    main()
