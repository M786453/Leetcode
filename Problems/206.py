# Problem#206. Reverse Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head : ListNode):
        # Time Complexity: Beats 100%
        # Space Complexity: Beats 74.01%
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        prev = None
        curr = head
        
        while curr:

            tmp = curr.next

            curr.next = prev

            prev = curr

            curr = tmp

        return curr

# linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# ss = Solution()

# ss.reverseList(linked_list)


            

            
            





        