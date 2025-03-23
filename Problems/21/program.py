class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(given_list):

    linked_list = None

    for n in given_list:

        if linked_list:

            node = linked_list

            while node.next:
                node = node.next
            
            node.next = ListNode(n, None)

        else:
            linked_list = ListNode(n, None)

    return linked_list

def add_element(val, linked_list):

    if linked_list:

        node = linked_list

        while node.next:
            node = node.next
        
        node.next = ListNode(val, None)

    else:
        linked_list = ListNode(val, None)

    return linked_list

def print_linked_list(linked_list):

    node = linked_list

    while node:
        print(node.val, end=" ")
        node = node.next
    
def mergeTwoLists(list1, list2):

    list1 = create_linked_list(list1)

    list2 = create_linked_list(list2)

    merged_list = None
    
    while list1 or list2:

        if list1 and list2:
            
            if list1.val == list2.val:


                merged_list = add_element(list1.val, merged_list)
                merged_list = add_element(list2.val, merged_list)


                list1 = list1.next
                list2 = list2.next
        
            elif list1.val < list2.val:

                merged_list = add_element(list1.val, merged_list)
                list1 = list1.next

            elif list2.val < list1.val:

                merged_list = add_element(list2.val, merged_list)
                list2 = list2.next
            
        else:

            if list1:
                merged_list = add_element(list1.val, merged_list)
                list1 = list1.next
            else:
                merged_list = add_element(list2.val, merged_list)
                list2 = list2.next
                

    return merged_list

print_linked_list(mergeTwoLists(list1 = [], list2 = [0,1,2,3]))




    