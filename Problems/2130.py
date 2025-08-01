# Leetcode Problem#2130. Maximum Twin Sum of a Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def pairSum(self, head: ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        size = 0

        arr = []

        node = head

        while node:

            arr.append(node.val)

            node = node.next

            size += 1

        max = 0

        for i in range(size//2):

            pair_sum = arr[i] + (arr[size - 1 - i])

            if pair_sum > max:
                max = pair_sum

        return max


head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))

ss = Solution()

print("Answer:",ss.pairSum(head=head))
        