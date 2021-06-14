# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    while current is not None:
        nextDistinctNode = current.next
        while nextDistinctNode is not None and nextDistinctNode.value == current.value :
            nextDistinctNode = nextDistinctNode.next
        current.next = nextDistinctNode
        current = nextDistinctNode
    return linkedList