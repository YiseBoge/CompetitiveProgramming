from LeetCode.LinkedList.__list_node__ import ListNode
from LeetCode.LinkedList.__list_node__ import print_list


def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


def solution(l1):
    delete_node(l1)


def main():
    inp1 = ListNode(4)
    inp2 = ListNode(5)
    inp3 = ListNode(2)
    inp1.next = inp2
    inp2.next = inp3

    solution(inp2)
    print_list(inp1)


if __name__ == '__main__':
    main()
