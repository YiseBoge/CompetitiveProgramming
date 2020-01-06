from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def __init__(self):
        self.max = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.count_path(root)
        return self.max

    def count_path(self, node):
        if node == None:
            return 0

        l = self.count_path(node.left)
        r = self.count_path(node.right)

        if node.left is not None and node.left.val == node.val:
            l += 1
        else:
            l = 0

        if node.right is not None and node.right.val == node.val:
            r += 1
        else:
            r = 0

        self.max = max(self.max, l + r)
        return max(l, r)


def solution(l1):
    s = Solution()
    return s.longestUnivaluePath(l1)


def main():
    inp1 = TreeNode(3)
    inp2 = TreeNode(5)
    inp3 = TreeNode(3)
    inp1.right = inp2
    inp1.left = inp3

    print(solution(inp1))


if __name__ == '__main__':
    main()
