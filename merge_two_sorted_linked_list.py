# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_node = ListNode(0)
        current_node = temp_node

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list1 = list1.next

            current_node = current_node.next

        current_node.next = list1 or list2

        return temp_node.next