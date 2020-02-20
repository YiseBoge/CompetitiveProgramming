from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def __init__(self):
        self.moves = 0

    def distributeCoins(self, root: TreeNode) -> int:
        self.do_moves(root)
        return self.moves

    def do_moves(self, root):
        current = root.val
        r, l = 0, 0
        if root.left:
            l = self.do_moves(root.left)

        if root.right:
            r = self.do_moves(root.right)

        current += l + r
        self.moves += abs(l) + abs(r)
        return current - 1


def solution(l1):
    s = Solution()
    return s.distributeCoins(l1)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(5)
    inp3 = TreeNode(3)
    inp1.right = inp2
    inp1.left = inp3

    print(solution(inp1))


if __name__ == '__main__':
    main()
