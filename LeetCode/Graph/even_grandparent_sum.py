from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0

        so_far = 0
        if root.val % 2 == 0:
            l, r = root.left, root.right

            if l:
                if l.left:
                    so_far += l.left.val
                if l.right:
                    so_far += l.right.val
            if r:
                if r.left:
                    so_far += r.left.val
                if r.right:
                    so_far += r.right.val

        return so_far + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)


def solution(l1):
    s = Solution()
    return s.sumEvenGrandparent(l1)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(2)
    inp3 = TreeNode(3)
    inp1.left = inp2
    inp2.right = inp3

    print(solution(inp1))


if __name__ == '__main__':
    main()
