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
        
        # Populate Stack

        st = []

        node = head

        while node:            

            st.append(node)

            node = node.next

        # Reverse linked list

        head = None

        node = None

        while st:

            if node:

                node.next = st.pop()

                node = node.next

            else:

                node = st.pop()

            if not head:
                head = node
        
        node.next = None # Tail of reverse list

class Solution2(object):
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

linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ss = Solution2()

ss.reverseList(linked_list)


            

            
            





        