import collections

from LeetCode.Graph.__graph_node__ import Employee


class Solution:
    def getImportance(self, employees: list, id: int) -> int:
        result = 0
        employee_collection = {}
        visited_employee_ids = {id}

        for employee in employees:
            employee_collection[employee.id] = employee

        queue = collections.deque([id])
        visited_employee_ids.add(id)

        while queue:
            current_id = queue.popleft()
            current_employee = employee_collection[current_id]
            result += current_employee.importance

            for sub_id in current_employee.subordinates:
                if sub_id not in visited_employee_ids:
                    queue.append(sub_id)
                    visited_employee_ids.add(sub_id)

        return result


def solution(l1, l2):
    s = Solution()
    return s.getImportance(l1, l2)


def main():
    inp1 = [
        Employee(1, 10, [2, 3]),
        Employee(2, 5, []),
        Employee(3, 3, [])
    ]
    inp = 1

    print(solution(inp1, inp))


if __name__ == '__main__':
    main()
