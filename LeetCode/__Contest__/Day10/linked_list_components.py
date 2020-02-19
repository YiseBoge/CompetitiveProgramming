from LeetCode.LinkedList.__list_node__ import ListNode


class Solution:
    def numComponents(self, head: ListNode, G: list) -> int:
        result = 0
        possibles = set(G)

        buffer = []
        h = head
        while h:
            if h.val in possibles:
                buffer.append(h.val)
            else:
                result += min(len(buffer), 1)
                buffer = []
            h = h.next
        result += min(len(buffer), 1)
        return result


def solution(l1, l2):
    s = Solution()
    return s.numComponents(l1, l2)


def main():
    inp1 = ListNode(0)
    inp1.next = ListNode(1)
    inp1.next.next = ListNode(2)
    inp1.next.next.next = ListNode(3)
    inp1.next.next.next.next = ListNode(4)
    inp2 = [0, 3, 1, 4]

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
