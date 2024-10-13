class Deque:
    def __init__(self):
        self.deque = []

    # Add an element to the front
    def add_front(self, value):
        self.deque.insert(0, value)

    # Add an element to the rear
    def add_rear(self, value):
        self.deque.append(value)

    # Remove an element from the front
    def remove_front(self):
        if not self.is_empty():
            return self.deque.pop(0)
        return "Deque is empty"

    # Remove an element from the rear
    def remove_rear(self):
        if not self.is_empty():
            return self.deque.pop()
        return "Deque is empty"

    # Check if the deque is empty
    def is_empty(self):
        return len(self.deque) == 0

# Example usage
dq = Deque()
dq.add_front(10)
dq.add_rear(20)
print(dq.remove_front())  # Output: 10
print(dq.remove_rear())   # Output: 20
