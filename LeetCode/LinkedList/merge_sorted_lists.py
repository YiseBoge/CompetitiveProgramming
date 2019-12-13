from LeetCode.LinkedList.__list_node__ import ListNode
from LeetCode.LinkedList.__list_node__ import print_list


def reverse_list(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    if l1.val > l2.val:
        result = ListNode(l2.val)
        l2 = l2.next
    else:
        result = ListNode(l1.val)
        l1 = l1.next
    r = result

    while l1 is not None or l2 is not None:
        if l2 is None:
            r.next = ListNode(l1.val)
            l1 = l1.next
        elif l1 is None:
            r.next = ListNode(l2.val)
            l2 = l2.next
        else:
            if l1.val > l2.val:
                r.next = ListNode(l2.val)
                l2 = l2.next
            else:
                r.next = ListNode(l1.val)
                l1 = l1.next
        r = r.next
    return result


def solution(l1, l2):
    return reverse_list(l1, l2)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = ListNode(1)
    inp1.next = ListNode(3)

    inp2 = ListNode(2)
    inp2.next = ListNode(5)

    print_list(solution(inp1, inp2))


if __name__ == '__main__':
    main()
