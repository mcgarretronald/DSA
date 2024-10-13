#Implement a circular queue, which wraps around when the queue reaches the end of the array.
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    # Add an element to the queue
    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            return "Queue is full"
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    # Remove an element from the queue
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    # Peek at the front element of the queue
    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]
        return "Queue is empty"

    # Check if the queue is empty
    def is_empty(self):
        return self.front == -1

# Example usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print(cq.dequeue())  # Output: 10
cq.enqueue(40)
cq.enqueue(50)
print(cq.peek())     # Output: 20
