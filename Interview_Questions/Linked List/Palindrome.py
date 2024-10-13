# Definition for a singly linked list node
#Given the head of a singly linked list, return true if it is a palindrome.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to check if a linked list is a palindrome
def is_palindrome(head):
    slow = fast = head
    stack = []
    
    # Use a slow and fast pointer to find the middle
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    
    # Skip the middle element for odd length linked lists
    if fast:
        slow = slow.next

    # Compare the second half with the reversed first half
    while slow:
        if slow.value != stack.pop():
            return False
        slow = slow.next

    return True

# Example usage
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(is_palindrome(head))  # Output: True
