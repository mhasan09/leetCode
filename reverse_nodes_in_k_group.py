class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_at_the_end_of_linked_list(head, val):
    node = ListNode(val)
    if head is None:
        head = node
        return head

    temp = head
    while temp.next is not None:
        temp = temp.next

    temp.next = node
    return head


def printLinkedList(head):
    while head.next is not None:
        print(head.val, end="->")
        head = head.next
    print(head.val)


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1


        if count < k:
            return head

        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = self.reverseKGroup(curr, k)
        return prev


if __name__ == "__main__":
    head = None
    k = 2
    head = insert_at_the_end_of_linked_list(head, 1)
    head = insert_at_the_end_of_linked_list(head, 2)
    head = insert_at_the_end_of_linked_list(head, 3)


    print("Original Linked List: ", end="")
    printLinkedList(head)
    print("After Reversal of k nodes: ", end="")
    newHead = Solution().reverseKGroup(head, k)
    printLinkedList(newHead)