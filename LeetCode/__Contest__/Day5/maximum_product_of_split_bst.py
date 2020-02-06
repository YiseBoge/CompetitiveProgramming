from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def __init__(self):
        self.sums = {}
        self.product = 0

    def maxProduct(self, root: TreeNode) -> int:
        total = self.calculate_sum(root)
        self.do_product(root, total)

        return self.product % (10 ** 9 + 7)

    def do_product(self, root, total):

        if root.left:
            s = self.sums[root.left]
            product = (s * (total - s))
            self.product = max(product, self.product)
            self.do_product(root.left, total)

        if root.right:
            s = self.sums[root.right]
            product = (s * (total - s))
            self.product = max(product, self.product)
            self.do_product(root.right, total)

    def calculate_sum(self, root):
        if not root:
            return 0

        current = root.val
        current += self.calculate_sum(root.left)
        current += self.calculate_sum(root.right)

        self.sums[root] = current
        return current


def solution(l1):
    s = Solution()
    return s.maxProduct(l1)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(5)
    inp3 = TreeNode(3)
    inp1.right = inp2
    inp1.left = inp3

    print(solution(inp1))


if __name__ == '__main__':
    main()
