from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        root = TreeNode(preorder[0])
        self.build_nodes(root, preorder, 0, preorder[0])
        return root

    def build_nodes(self, parent, items, index, value):
        # print(items[index])

        right_index = None
        for i in range(index, len(items)):
            if items[i] is not None and items[i] > value:
                right_index = i
                break

        if right_index is not None:
            right_val = items[right_index]
            right_node = TreeNode(right_val)
            parent.right = right_node

            items[right_index] = None
            self.build_nodes(right_node, items, right_index, right_val)

        left_index = index + 1
        if left_index < len(items) and items[left_index] is not None and items[left_index] < value:
            left_val = items[left_index]
            left_node = TreeNode(left_val)
            parent.left = left_node

            items[left_index] = None
            self.build_nodes(left_node, items, left_index, left_val)


def solution(l1):
    s = Solution()
    return s.bstFromPreorder(l1)


def main():
    inp1 = [8, 5, 1, 7, 11, 12]

    print(solution(inp1))


if __name__ == '__main__':
    main()
