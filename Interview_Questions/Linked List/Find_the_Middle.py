# Definition for a singly linked list node
#Given the head of a singly linked list, return the middle node of the list.
# If there are two middle nodes, return the second middle node.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to find the middle of the linked list
def find_middle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
middle_node = find_middle(head)
print(middle_node.value)  # Output: 3
