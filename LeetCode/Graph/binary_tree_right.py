from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def __init__(self):
        self.results = {}

    def rightSideView(self, root: TreeNode) -> list:
        r = []
        if not root:
            return []
        self.do_dfs(root, 0)
        for i in self.results:
            r.append(self.results[i])
        return r

    def do_dfs(self, root, depth):
        self.results[depth] = root.val
        if not (root.left or root.right):
            return
        if root.left:
            self.do_dfs(root.left, depth + 1)
        if root.right:
            self.do_dfs(root.right, depth + 1)


def solution(l1):
    s = Solution()
    return s.rightSideView(l1)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(2)
    inp3 = TreeNode(3)
    inp1.left = inp2
    inp2.right = inp3

    print(solution(inp1))


if __name__ == '__main__':
    main()
