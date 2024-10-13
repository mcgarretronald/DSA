#Implement a basic stack with push, pop, peek, and isEmpty operations.
class Stack:
    def __init__(self):
        self.stack = []
    
    # Push an element to the top of the stack
    def push(self, value):
        self.stack.append(value)
    
    # Pop an element from the top of the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    # Peek the top element of the stack
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())  # Output: 30
print(s.pop())   # Output: 30
print(s.pop())   # Output: 20
print(s.is_empty())  # Output: False
