from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def __init__(self):
        self.results = set()
        self.sums = {}
        self.max_frequency = 0

    def findFrequentTreeSum(self, root: TreeNode):
        self.sum_finder(root)
        return self.results

    def sum_finder(self, root: TreeNode):
        if not root:
            return 0
        current_sum = root.val + self.sum_finder(root.left) + self.sum_finder(root.right)

        if self.sums.get(current_sum) is None:
            self.sums[current_sum] = 1
        else:
            self.sums[current_sum] += 1

        current_frequency = self.sums[current_sum]
        if current_frequency == self.max_frequency:
            self.results.add(current_sum)
        elif current_frequency > self.max_frequency:
            self.results = {current_sum}
            self.max_frequency = current_frequency

        return current_sum


def solution(l1):
    s = Solution()
    return s.findFrequentTreeSum(l1)


def main():
    inp1 = TreeNode(1)
    inp2 = TreeNode(2)
    inp3 = TreeNode(3)
    inp1.left = inp2
    inp2.right = inp3

    print(solution(inp1))


if __name__ == '__main__':
    main()
