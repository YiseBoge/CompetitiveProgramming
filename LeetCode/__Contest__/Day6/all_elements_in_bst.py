from LeetCode.BST.__tree_node__ import TreeNode


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list:
        result1 = []
        result2 = []
        result = []
        self.traverse(root1, result1)
        self.traverse(root2, result2)

        ind1 = 0
        ind2 = 0
        while ind1 < len(result1) or ind2 < len(result2):
            if ind1 >= len(result1):
                result.append(result2[ind2])
                ind2 += 1
            elif ind2 >= len(result2):
                result.append(result1[ind1])
                ind1 += 1
            else:
                if result1[ind1] < result2[ind2]:
                    result.append(result1[ind1])
                    ind1 += 1
                elif result1[ind1] > result2[ind2]:
                    result.append(result2[ind2])
                    ind2 += 1
                else:
                    result.append(result1[ind1])
                    result.append(result2[ind2])
                    ind1 += 1
                    ind2 += 1

        return result

    def traverse(self, root, collection):
        if not root:
            return
        self.traverse(root.left, collection)
        collection.append(root.val)
        self.traverse(root.right, collection)


def solution(l1, l2):
    s = Solution()
    return s.getAllElements(l1, l2)


def main():
    inp1 = TreeNode(4)
    inp2 = TreeNode(5)
    inp3 = TreeNode(3)
    inp4 = TreeNode(1)
    inp1.right = inp2
    inp3.left = inp4

    print(solution(inp1, inp3))


if __name__ == '__main__':
    main()
