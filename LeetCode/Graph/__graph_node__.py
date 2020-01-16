class Node:
    def __init__(self, val=None, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

    def __str__(self):
        returnable = str(self.val) + " -> " + str(self.children)
        return returnable
