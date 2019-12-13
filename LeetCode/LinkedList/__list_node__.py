class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def print_list(lst: ListNode):
    l = lst
    result = "["
    while l is not None and l.next is not None:
        result += (str(l.val) + ", ")
        l = l.next

    result += (str(l.val) + "]") if l is not None else "]"

    print(result)
