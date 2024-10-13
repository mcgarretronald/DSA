#Implement a priority queue where elements with higher priorities are dequeued before lower-priority elements.
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    # Enqueue an element with a priority
    def enqueue(self, value, priority):
        heapq.heappush(self.queue, (priority, value))
    
    # Dequeue the element with the highest priority
    def dequeue(self):
        if self.queue:
            return heapq.heappop(self.queue)[1]
        return "Queue is empty"

# Example usage
pq = PriorityQueue()
pq.enqueue("Task 1", 2)
pq.enqueue("Task 2", 1)
pq.enqueue("Task 3", 3)
print(pq.dequeue())  # Output: "Task 2"
print(pq.dequeue())  # Output: "Task 1"
