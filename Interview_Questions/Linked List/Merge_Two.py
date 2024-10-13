# Definition for a singly linked list node
#Given the heads of two sorted linked lists, merge them into one sorted linked list and return the merged list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to merge two sorted linked lists
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2  # Append the remaining nodes
    return dummy.next

# Example usage
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
merged_head = merge_two_lists(l1, l2)

# Print merged list
while merged_head:
    print(merged_head.value, end=" -> ")
    merged_head = merged_head.next
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 
