class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Linkedlist:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            return
        current_node = self.head

        while True:
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.val} ->",end=" ")
            current_node = current_node.next
        print(None)

ll = Linkedlist()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.print_linked_list()