from LeetCode.Graph.__graph_node__ import Node


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maximum = 1
        for child in root.children:
            j = 1 + self.maxDepth(child)
            if j > maximum:
                maximum = j
        return maximum


def solution(l1):
    s = Solution()
    return s.maxDepth(l1)


def main():
    inp1 = Node(1)
    inp2 = Node(2)
    inp3 = Node(3)
    inp1.children = [inp2, inp3]

    print(solution(inp1))


if __name__ == '__main__':
    main()
