#Given a string, reverse it using a stack.
def reverse_string(s):
    stack = []
    
    # Push all characters of string to the stack
    for char in s:
        stack.append(char)
    
    # Pop all characters from the stack and form the reversed string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str

# Example usage
print(reverse_string("hello"))  # Output: "olleh"
