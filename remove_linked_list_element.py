# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        if not head:
            return head

        itr = head
        while itr:
            if itr.next and itr.next.val == val:
                itr.next = itr.next.next
            else:
                itr = itr.next

        return head
