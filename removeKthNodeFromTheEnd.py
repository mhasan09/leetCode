# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    first = second = head
    counter = 1
    while counter <= k:
        counter += 1
        second = second.next

    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while second.next is not None:
        second = second.next
        first = first.next

    first.next = first.next.next
