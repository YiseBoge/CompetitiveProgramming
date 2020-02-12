import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        results = set()
        graph = {}
        incomings = [0] * numCourses

        for i in range(numCourses):
            graph[i] = []

        for el in prerequisites:
            incomings[el[1]] += 1
            graph[el[0]].append(el[1])

        queue = collections.deque()
        for i in range(len(incomings)):
            if incomings[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            if current in results:
                return False
            results.add(current)

            for n in graph[current]:
                incomings[n] -= 1
                if incomings[n] == 0:
                    queue.append(n)
        return len(results) == numCourses


def solution(l1, l2):
    s = Solution()
    return s.canFinish(l1, l2)


def main():
    inp1 = 2
    inp2 = [[1, 0], [0, 1]]

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
