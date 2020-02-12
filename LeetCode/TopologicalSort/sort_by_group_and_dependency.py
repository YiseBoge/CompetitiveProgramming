import collections
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = {}
        group_dependencies = [0] * m
        num_dependencies = [0] * n
        results = []
        for i in range(-1, m):
            groups[i] = []

        visited_groups = set()
        for i in range(n):
            groups[group[i]].append(i)
            num_dependencies[i] = len(beforeItems[i])
            g = group[i]
            for b in beforeItems[i]:
                d = group[b]
                if g != d and g > -1 and d > -1 and (g, d) not in visited_groups:
                    group_dependencies[g] += 1
                    visited_groups.add((g, d))

        group_queue = collections.deque()
        num_queue = collections.deque()

        for i in range(len(num_dependencies)):
            val = num_dependencies[i]
            if val == 0 and group[i] == -1:
                num_queue.append(i)

        for i in range(len(group_dependencies)):
            val = group_dependencies[i]
            if val == 0:
                group_queue.append(i)

        while group_queue or num_queue:
            # print(results, num_queue, group_queue)
            if num_queue:
                current = num_queue.popleft()
                results.append(current)
                for i in range(n):
                    if current not in beforeItems[i]:
                        continue
                    g = group[i]
                    num_dependencies[i] -= 1
                    group_dependencies[g] -= 1
                    if num_dependencies[i] < 0:
                        return []
                    if num_dependencies[i] == 0 and group[i] == -1:
                        num_queue.append(i)
                    if group_dependencies[g] == 0 and g > -1:
                        group_queue.append(g)
            else:
                current = group_queue.popleft()
                fixed = self.sort_group(num_dependencies, group_dependencies, current, group, beforeItems, group_queue,
                                        num_queue)
                if current > 400:
                    print(current, groups[current], fixed)
                if len(fixed) != len(groups[current]):
                    return []

                for i in fixed:
                    results.append(i)
        return results if len(results) == n else []

    def sort_group(self, num_dependencies, group_dependencies, g, group, beforeItems, group_queue, num_queue):
        result = []
        queue = collections.deque()
        for i in range(len(num_dependencies)):
            if group[i] == g and num_dependencies[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            result.append(current)

            for i in range(len(num_dependencies)):
                if current not in beforeItems[i]:
                    continue
                gr = group[i]
                num_dependencies[i] -= 1
                group_dependencies[gr] -= 1
                if num_dependencies[i] < 0:
                    return []
                if num_dependencies[i] == 0 and gr == g:
                    queue.append(i)
                elif num_dependencies[i] == 0 and gr == -1:
                    num_queue.append(i)
                if group_dependencies[gr] == 0 and gr > -1:
                    group_queue.append(gr)
        # print(g, result)
        return result


def solution(l1, l2, l3, l4):
    s = Solution()
    return s.sortItems(l1, l2, l3, l4)


def main():
    inp1 = 8
    inp2 = 2
    inp3 = [-1, -1, 1, 0, 0, 1, 0, -1]
    inp4 = [[], [6], [5], [6], [3, 6], [], [], []]

    print(solution(inp1, inp2, inp3, inp4))


if __name__ == '__main__':
    main()
