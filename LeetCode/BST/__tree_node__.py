# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_tree(root):
    if root is None:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)
