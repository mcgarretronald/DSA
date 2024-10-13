#Sort a stack in ascending order using only recursion (no additional data structures are allowed)
def insert_sorted(stack, element):
    if len(stack) == 0 or element > stack[-1]:
        stack.append(element)
    else:
        temp = stack.pop()
        insert_sorted(stack, element)
        stack.append(temp)

def sort_stack(stack):
    if len(stack) > 0:
        temp = stack.pop()
        sort_stack(stack)
        insert_sorted(stack, temp)

# Example usage
stack = [34, 3, 31, 98, 92, 23]
sort_stack(stack)
print(stack)  # Output: [3, 23, 31, 34, 92, 98]
