from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        maximum = 0
        for i in range(len(nums)):
            if nums[i] > nums[maximum]:
                maximum = i
        root = TreeNode(nums[maximum])

        left_sub = nums[:maximum]
        right_sub = nums[maximum + 1:]

        if len(left_sub) > 0:
            root.left = self.constructMaximumBinaryTree(left_sub)
        if len(right_sub) > 0:
            root.right = self.constructMaximumBinaryTree(right_sub)

        return root


def solution(l1):
    s = Solution()
    return s.constructMaximumBinaryTree(l1)


def main():
    inp1 = [3, 2, 1, 6, 0, 5]
    print(solution(inp1))


if __name__ == '__main__':
    main()
