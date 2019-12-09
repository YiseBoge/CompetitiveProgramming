from LeetCode.LinkedList.list_node import ListNode


def print_list(lst):
    l = lst.head
    result = "["
    while l is not None and l.next is not None:
        result += (str(l.val) + ", ")
        l = l.next

    result += (str(l.val) + "]") if l is not None else "]"

    print(result)


class MyLinkedList:

    def __init__(self):
        self.head: ListNode = None
        self.tail: ListNode = None

    def get(self, index: int) -> int:
        h = self.head

        i = 0
        while h is not None:
            if i == index and h.val is not None:
                return h.val
            h = h.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        n = ListNode(val)
        n.next = self.head
        self.head = n
        if self.tail is None:
            self.tail = n

    def addAtTail(self, val: int) -> None:
        n = ListNode(val)
        if self.tail is None:
            self.tail = n
            self.head = n
            return
        self.tail.next = n
        self.tail = n

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        h = self.head
        i = 0
        if h is None:
            return
        while h.next is not None:
            if i + 1 == index:
                n = ListNode(val)
                n.next = h.next
                h.next = n
                return
            h = h.next
            i += 1

        if i + 1 == index:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                self.tail = None if self.head is None else self.tail
            return

        h = self.head

        if h is None or h.next is None:
            return
        i = 0
        while h.next.next is not None:
            if i + 1 == index:
                h.next = h.next.next
                return
            h = h.next
            i += 1
        if i + 1 == index:
            h.next = None
            self.tail = h


if __name__ == '__main__':
    obj = MyLinkedList()
    index = 0
    obj.deleteAtIndex(index)
    print_list(obj)

    index = 0
    print(obj.get(index))

    val = 10
    obj.addAtHead(val)
    print_list(obj)

    index = 0
    val = 2
    obj.addAtIndex(index, val)
    print_list(obj)

    index = 1
    val = 1
    obj.addAtIndex(index, val)
    print_list(obj)

    index = 10
    val = 3
    obj.addAtIndex(index, val)
    print_list(obj)

    val = 4
    obj.addAtTail(val)
    print_list(obj)
    val = 5
    obj.addAtTail(val)
    print_list(obj)

    index = 0
    obj.deleteAtIndex(index)
    print_list(obj)

    val = 4
    obj.addAtTail(val)
    print_list(obj)

    index = 0
    print(obj.get(index))
