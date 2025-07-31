# Problem#328: Odd Even Linked List

class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def oddEvenList(self, head : ListNode):

        if not head or not head.next:

            return head
        
        odd, even = head, head.next

        even_head = even

        while even and even.next:

            odd.next, even.next = odd.next.next, even.next.next

            odd, even = odd.next, even.next

        odd.next = even_head

        return head


if __name__ == "__main__":

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    ss = Solution()

    ss.oddEvenList(head)

