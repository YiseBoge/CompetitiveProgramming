from LeetCode.BST.__tree_node__ import TreeNode

minimum = None
maximum = None


class Solution:
    def __init__(self):
        self.min = None
        self.max = None

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.min = L
        self.max = R
        return self.go_through(root)

    def go_through(self, root):
        result = 0

        if self.min <= root.val <= self.max:
            result += root.val

        if root.left is not None and root.val > self.min:
            result += self.go_through(root.left)

        if root.right is not None and root.val < self.max:
            result += self.go_through(root.right)

        return result


def solution(l1, l2, l3):
    s = Solution()
    return s.rangeSumBST(l1, l2, l3)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(5)
    inp3 = TreeNode(2)

    inp1.left = inp2
    inp2.right = inp3

    print(solution(inp1, 3, 6))


if __name__ == '__main__':
    main()
