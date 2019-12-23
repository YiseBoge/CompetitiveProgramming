from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val == p.val or root.val == q.val:
            return root

        if root.val < p.val and root.val < q.val:
            return self.lowest_common_ancestor(root.right, p, q)

        if root.val > p.val and root.val > q.val:
            return self.lowest_common_ancestor(root.left, p, q)

        return root


def solution(l1, l2, l3):
    s = Solution()
    return s.lowest_common_ancestor(l1, l2, l3)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(5)
    inp3 = TreeNode(3)
    inp1.right = inp2
    inp1.left = inp3

    print(solution(inp1, inp2, inp3))


if __name__ == '__main__':
    main()
