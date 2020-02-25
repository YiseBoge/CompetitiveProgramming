import heapq

from LeetCode.LinkedList.__list_node__ import ListNode


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        result = ListNode(None)
        all_nodes = []
        heap = []
        for lst in lists:
            if lst:
                all_nodes.append(lst)
                heapq.heappush(heap, (lst.val, len(all_nodes) - 1))

        r = result
        while heap:
            current = heapq.heappop(heap)
            node = all_nodes[current[1]]
            new = node.next
            all_nodes.append(new)
            r.next = node
            r = r.next
            if new:
                heapq.heappush(heap, (new.val, len(all_nodes) - 1))
        return result.next


def solution(l1):
    s = Solution()
    return s.mergeKLists(l1)


def main():
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(3)
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)
    inp1 = [l1, l2]
    print(solution(inp1))


if __name__ == '__main__':
    main()
