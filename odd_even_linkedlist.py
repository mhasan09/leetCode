from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode()
        odd_tail = odd_head

        even_head = ListNode()
        even_tail = even_head

        i = 1

        while head:
            if i & 1:
                odd_tail.next = head
                odd_tail = odd_tail.next
                head = head.next
                odd_tail.next = None
            else:
                even_tail.next = head
                even_tail = even_tail.next
                head = head.next
                even_tail.next = None
            i += 1

        odd_tail.next = even_head.next
        return odd_head.next


if __name__ == "__main__":
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = None

    out = Solution().odd_even_list(one)
    while out:
        print(out.val)
        out = out.next




