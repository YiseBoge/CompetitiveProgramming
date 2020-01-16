from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        current_sum = sum - root.val
        if not root.left and not root.right:
            return current_sum == 0

        return self.hasPathSum(root.left, current_sum) or self.hasPathSum(root.right, current_sum)


def solution(l1, l2):
    s = Solution()
    return s.hasPathSum(l1, l2)


def main():
    inp1 = TreeNode(1)
    inp2 = TreeNode(2)
    inp3 = TreeNode(3)
    inp1.left = inp2
    inp2.right = inp3

    inp = 6

    print(solution(inp1, inp))


if __name__ == '__main__':
    main()
