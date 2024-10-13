#Implement a basic queue with enqueue, dequeue, peek, and isEmpty operations.
class Queue:
    def __init__(self):
        self.queue = []
    
    # Add an element to the back of the queue
    def enqueue(self, value):
        self.queue.append(value)
    
    # Remove an element from the front of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"
    
    # Peek at the front element of the queue
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"
    
    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.peek())  # Output: 10
print(q.dequeue())  # Output: 10
print(q.dequeue())  # Output: 20
print(q.is_empty())  # Output: False
