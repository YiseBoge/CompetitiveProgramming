from LeetCode.LinkedList.__list_node import ListNode


def print_list(lst: ListNode):
    l = lst
    result = "["
    while l is not None and l.next is not None:
        result += (str(l.val) + ", ")
        l = l.next

    result += (str(l.val) + "]") if l is not None else "]"

    print(result)


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
    print_list(solution(inp1))


if __name__ == '__main__':
    main()
