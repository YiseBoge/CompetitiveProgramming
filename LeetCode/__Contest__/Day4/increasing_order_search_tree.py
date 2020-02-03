from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def __init__(self):
        self.result = None

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.result = None
        self.go_through(root)
        return self.result

    def go_through(self, root: TreeNode):
        if root.left:
            self.go_through(root.left)

        new = TreeNode(root.val)
        if not self.result:
            new.right = self.result
            self.result = new
        else:
            self.insert_into_result(new)

        if root.right:
            self.go_through(root.right)

    def insert_into_result(self, new):
        r = self.result
        while r.right:
            r = r.right
        r.right = new


def solution(l1):
    s = Solution()
    return s.increasingBST(l1)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(5)
    inp3 = TreeNode(3)
    inp1.right = inp2
    inp1.left = inp3

    print(solution(inp1))


if __name__ == '__main__':
    main()
