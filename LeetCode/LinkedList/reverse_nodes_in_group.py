from LeetCode.LinkedList.__list_node__ import ListNode


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    handle = ListNode(None)
    handle.next = head
    do_reverse(handle, k)
    return handle.next


def do_reverse(handle: ListNode, k):
    if handle is None or not big_enough(handle.next, k):
        return
    h = handle.next
    last = handle
    num = k
    while num > 0:
        next_node = h.next
        h.next = last
        last = h
        h = next_node
        num -= 1
    v = handle.next
    v.next = h
    handle.next = last
    do_reverse(v, k)


def big_enough(node: ListNode, k):
    if k <= 0:
        return False
    count = 0
    h = node
    while h is not None:
        count += 1
        if count >= k:
            return True
        h = h.next

    return False


def solution(l1, l2):
    return reverse_k_group(l1, l2)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = ListNode(1)
    inp1.next = ListNode(2)
    inp1.next.next = ListNode(3)
    inp1.next.next.next = ListNode(4)
    inp1.next.next.next.next = ListNode(5)

    inp2 = 2

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
