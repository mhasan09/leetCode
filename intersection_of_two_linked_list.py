# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        itr1 = headA
        itr2 = headB
        if headA is None or headB is None:
            return
        while itr1 != itr2:
            if itr1 is None:
                itr1 = headB
            else:
                itr1 = itr1.next
            if itr2 is None:
                itr2 = headA
            else:
                itr2 = itr2.next
        return itr1

