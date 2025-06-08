# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        len_count = 1
        current = head
        while current.next is not None:
            len_count += 1

        need_to_rotate = k % len_count
        if need_to_rotate == 0:
            return head

        prev = None
        current = head
        for _ in range(need_to_rotate):
            while current.next is not None:
                prev = current
                current = current.next

            prev.next = None
            current.next = head
            head = current

        return head


