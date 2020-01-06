from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def find_bottom_left_value(self, root: TreeNode) -> int:
        start_level = 0
        r = self.look_for_lower(root, start_level)
        return r[0]

    def look_for_lower(self, node, level):
        if node.left is None and node.right is None:
            return node.val, level

        r = node.val, level
        l = node.val, level

        if node.left is not None:
            l = self.look_for_lower(node.left, level + 1)
        if node.right is not None:
            r = self.look_for_lower(node.right, level + 1)

        return r if r[1] > l[1] else l


def solution(l1):
    s = Solution()
    return s.find_bottom_left_value(l1)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(5)
    inp3 = TreeNode(3)
    inp1.right = inp2
    inp1.left = inp3

    print(solution(inp1))


if __name__ == '__main__':
    main()
