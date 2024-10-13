# Definition for a singly linked list node
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to reverse the linked list
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Store next node
        current.next = prev  # Reverse the current node's pointer
        prev = current  # Move pointers one position ahead
        current = next_node

    return prev  # New head of the reversed list

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reversed_head = reverse_linked_list(head)

# Print reversed list
while reversed_head:
    print(reversed_head.value, end=" -> ")
    reversed_head = reversed_head.next
# Output: 4 -> 3 -> 2 -> 1 -> 
