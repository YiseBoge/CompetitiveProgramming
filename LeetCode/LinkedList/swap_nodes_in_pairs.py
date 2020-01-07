from LeetCode.LinkedList.__list_node__ import ListNode


def swap_pairs(head: ListNode) -> ListNode:
    handle = ListNode(None)
    handle.next = head
    do_reverse(handle, 2)
    return handle.next


def do_reverse(handle: ListNode, k):
    if handle is None or not big_enough(handle.next, k):
        return
    h = handle.next
    # print("started at", handle)
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
    # print("finished with", handle)
    do_reverse(v, k)


def big_enough(node: ListNode, k):
    if k <= 0:
        return False
    count = 0
    h = node
    while h is not None:
        count += 1
        if count >= k:
            # print(count)
            return True
        h = h.next

    return False


def solution(l1):
    return swap_pairs(l1)


def main():
    inp1 = ListNode(1)
    inp1.next = ListNode(2)
    inp1.next.next = ListNode(3)
    inp1.next.next.next = ListNode(4)
    inp1.next.next.next.next = ListNode(5)

    print(solution(inp1))


if __name__ == '__main__':
    main()
