from LeetCode.LinkedList.__list_node__ import ListNode
from LeetCode.LinkedList.__list_node__ import print_list


def remove_duplicates(head):
    result = head
    while head is not None:
        if head.next is not None and head.next.val == head.val:
            head.next = head.next.next
        else:
            head = head.next
    return result


def solution(l1):
    return remove_duplicates(l1)


def main():
    inp1 = ListNode(0)
    inp1.next = ListNode(1)
    inp1.next.next = ListNode(1)
    print_list(solution(inp1))


if __name__ == '__main__':
    main()
