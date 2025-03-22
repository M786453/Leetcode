class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(given_list):

    linked_list = None

    for n in given_list:

        if linked_list:

            node = linked_list.next
            while node:
                print(node.val)
                node = node.next
            
            node = ListNode(n, None)

            print(node.val)

        else:
    
            linked_list = ListNode(n, None)
            
    return linked_list

def print_linked_list(linked_list):

    node = linked_list

    while node:
        print(node.val, end="")
        node = node.next
        print(node)
    
def mergeTwoLists(list1, list2):

    merged_list = []
    
    while list1 and list2:

        if list1[0] == list2[0]:

            merged_list.append(list1.pop(0))
            merged_list.append(list2.pop(0))
        
        elif list1[0] < list2[0]:

            merged_list.append(list1.pop(0))
        
        else:

            merged_list.append(list2.pop(0))

    return merged_list

# print("Answer:", mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))

linked_list = create_linked_list([1,2,4,5])

# print_linked_list(linked_list)




    