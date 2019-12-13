from typing import Optional

from LeetCode.BST.__tree_node__ import TreeNode
from LeetCode.BST.__tree_node__ import print_tree


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> Optional[TreeNode]:
        result = None

        if t1 is None and t2 is not None:
            result = TreeNode(t2.val)
        elif t2 is None and t1 is not None:
            result = TreeNode(t1.val)
        elif t1 is not None and t2 is not None:
            result = TreeNode(t1.val + t2.val)
        else:
            return None

        l1 = t1.left if t1 is not None else None
        l2 = t2.left if t2 is not None else None

        r1 = t1.right if t1 is not None else None
        r2 = t2.right if t2 is not None else None

        result.left = self.mergeTrees(l1, l2)
        result.right = self.mergeTrees(r1, r2)

        return result


def solution(l1, l2):
    s = Solution()
    return s.mergeTrees(l1, l2)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(5)
    inp3 = TreeNode(2)
    inp4 = TreeNode(6)

    inp1.left = inp2
    inp3.right = inp4

    print_tree(solution(inp1, inp2))


if __name__ == '__main__':
    main()
