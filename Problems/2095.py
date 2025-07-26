# 2095. Delete the Middle Node of a Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head : ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Calculate size

        size = 0

        node = head

        while node:

            size += 1

            node = node.next

        if size == 1:
            return None

        # Find mid

        mid = size // 2

        node = head

        while node:

            if mid == 1:

                if node.next and node.next.next:

                    node.next = node.next.next
                
                else:

                    if node.next == None:
                        node = None
                    else:
                        node.next = None

                break

            node = node.next

            mid -= 1
        

        node = head

        while node:

            print(node.val)

            node = node.next

head = ListNode(1)

ss = Solution()

ss.deleteMiddle(head=head)


        