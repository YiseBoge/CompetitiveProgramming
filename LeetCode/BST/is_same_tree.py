from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def solution(l1, l2):
    s = Solution()
    return s.is_same_tree(l1, l2)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(5)
    inp3 = TreeNode(2)
    inp4 = TreeNode(6)

    inp1.left = inp2
    inp3.right = inp4

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
