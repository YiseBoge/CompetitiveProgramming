from LeetCode.BST.__tree_node__ import TreeNode
from LeetCode.BST.__tree_node__ import print_tree


class Solution:
    def search_bst(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.search_bst(root.left, val)
        if root.val < val:
            return self.search_bst(root.right, val)


def solution(l1, l2):
    s = Solution()
    return s.search_bst(l1, l2)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(5)
    inp1.left = inp2

    inp3 = 5

    print_tree(solution(inp1, inp3))


if __name__ == '__main__':
    main()
