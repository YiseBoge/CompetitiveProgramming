import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        results = []
        visited = set()
        graph = {}
        incomings = [0] * numCourses

        for i in range(numCourses):
            graph[i] = []

        for el in prerequisites:
            incomings[el[0]] += 1
            graph[el[1]].append(el[0])

        queue = collections.deque()
        for i in range(len(incomings)):
            if incomings[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            if current in visited:
                return []
            results.append(current)
            visited.add(current)

            for n in graph[current]:
                incomings[n] -= 1
                if incomings[n] == 0:
                    queue.append(n)

        return results if len(results) == numCourses else []


def solution(l1, l2):
    s = Solution()
    return s.findOrder(l1, l2)


def main():
    inp1 = 4
    inp2 = [[1, 0], [2, 0], [3, 1], [3, 2]]

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
