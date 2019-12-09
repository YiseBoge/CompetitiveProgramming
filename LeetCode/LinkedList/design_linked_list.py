from LeetCode.LinkedList.__list_node import print_list


class ListNode:

    def __init__(self):
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        h = self
        result = -1

        i = 0
        while h is not None:
            if i == index and h.val is not None:
                return h.val
            h = h.next
            i += 1
        return result

    def addAtHead(self, val: int) -> None:
        if self.val is None:
            self.val = val
        else:
            l = ListNode()
            l.val = self.val
            l.next = self.next
            self.next = l
            self.val = val
            print(self.val)

    def addAtTail(self, val: int) -> None:
        h = self

        if self.val is None:
            self.val = val
        else:
            while h.next is not None:
                h = h.next
            n = ListNode()
            n.val = val
            h.next = n

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        h = self
        i = 0
        while h.next is not None:
            if i + 1 == index:
                n = ListNode()
                n.val = val
                n.next = h.next
                h.next = n
                return
            h = h.next
            i += 1
        if i + 1 == index:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.next is None:
                self.val = None
            else:
                self.val = self.next.val
                self.next = self.next.next
            return

        h = self
        for i in range(index):
            if h.next is None:
                break
            if h.next.next is None and i + 1 == index:
                h.next = None
                break
            if i + 1 == index:
                h.next = h.next.next
            h = h.next


if __name__ == '__main__':
    obj = ListNode()
    index = 0
    obj.deleteAtIndex(index)
    print_list(obj)

    index = 0
    print(obj.get(index))

    val = 1
    obj.addAtHead(val)
    val = 4
    obj.addAtHead(val)
    val = 3
    obj.addAtTail(val)

    print_list(obj)

    index = 1
    val = 2
    obj.addAtIndex(index, val)
    print_list(obj)

    index = 0
    obj.deleteAtIndex(index)
    print_list(obj)

    index = 3
    print(obj.get(index))
