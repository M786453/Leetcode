# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def findMid(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

        return slow

    def reverse(self, mid):

        prev = None
        tmp = mid

        while tmp:

            curr = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = curr

        return prev 

    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        mid = self.findMid(head=head) # Find middle node of linked list
        mid = self.reverse(mid=mid) # Reverse second half of linked list

        # Find max twin sum

        node1 = head # First Half head
        node2 = mid # Second half (reversed) head
        max_twin_sum = 0

        while node2:

            max_twin_sum = max(max_twin_sum, node1.val + node2.val) 

            node1 = node1.next
            node2 = node2.next

        return max_twin_sum
        