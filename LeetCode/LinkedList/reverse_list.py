from LeetCode.LinkedList.__list_node__ import ListNode
from LeetCode.LinkedList.__list_node__ import print_list


def reverse_list(head):
    result = None

    while head is not None:
        r = ListNode(head.val)
        r.next = result
        result = r
        head = head.next

    return result


def solution(l1):
    return reverse_list(l1)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = ListNode(4)
    inp1.next = ListNode(1)
    print_list(solution(inp1))


if __name__ == '__main__':
    main()
