# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow.next = self.reverse(slow.next)
        slow = slow.next
        dummy = head
        while slow is not None:
            if slow.val != dummy.val:
                return False
            slow = slow.next
            dummy = dummy.next

        return True

    @staticmethod
    def reverse(head):
        prev = None
        nxt = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev