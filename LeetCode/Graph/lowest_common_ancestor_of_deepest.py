from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.just_do_it(root, 0)[1]

    def just_do_it(self, root, depth):
        if not (root.left or root.right):
            return depth, root
        if root.left and not root.right:
            return self.just_do_it(root.left, depth + 1)
        if root.right and not root.left:
            return self.just_do_it(root.right, depth + 1)

        l = self.just_do_it(root.left, depth + 1)
        r = self.just_do_it(root.right, depth + 1)

        print(l, r)
        if l[0] == r[0]:
            return l[0], root

        return l if l[0] > r[0] else r


def solution(l1):
    s = Solution()
    return s.lcaDeepestLeaves(l1)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(2)
    inp3 = TreeNode(3)
    inp1.left = inp2
    inp2.right = inp3

    print(solution(inp1))


if __name__ == '__main__':
    main()
