# Interview Question:
# Given a sorted array, how would you efficiently find the index of a target element?
# Implement a binary search algorithm for this.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            low = mid + 1  # Move to the right half
        else:
            high = mid - 1  # Move to the left half

    return -1  # Target not found in the array

# Example usage
sorted_array = [5, 12, 22, 25, 34, 64, 90]
target = 25
index = binary_search(sorted_array, target)
print(f"Target {target} found at index {index}")
