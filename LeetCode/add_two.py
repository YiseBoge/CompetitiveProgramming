import sys


def __to_list_node(ls):
    result = None
    result_final = None
    for i in ls:
        if result is None:
            result = ListNode(i)
            result_final = result
        else:
            result.next = ListNode(i)
            result = result.next
    return result_final


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    if l1.val == 0 and l1.next is None:
        return l2
    elif l2.val == 0 and l1.next is None:
        return l1

    carry = 0
    n = l1.val + l2.val + carry
    carry = n // 10
    result = ListNode(n % 10)
    result_final = result

    while l1.next is not None or l2.next is not None:
        if l1.next is None:
            n = l2.next.val + carry
            carry = n // 10
            result.next = ListNode(n % 10)
            l2 = l2.next
        elif l2.next is None:
            n = l1.next.val + carry
            carry = n // 10
            result.next = ListNode(n % 10)
            l1 = l1.next
        else:
            n = l1.next.val + l2.next.val + carry
            carry = n // 10
            result.next = ListNode(n % 10)
            l1 = l1.next
            l2 = l2.next
        result = result.next
    if carry > 0:
        result.next = ListNode(carry)

    return result_final


nums = [20, 12, 41]
target = 9


def solution(l1, l2):
    return add_two_numbers(l1, l2)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = [1, 2, 3]
    inp2 = [3, 4, 5]
    in1 = __to_list_node(inp1)
    in2 = __to_list_node(inp2)
    sys.stdout.write(str(solution(in1, in2)))


if __name__ == '__main__':
    main()
