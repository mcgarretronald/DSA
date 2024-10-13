# Interview Question:
# Given a sorted array, remove the duplicates in-place so that each element appears only once.
# Return the new length of the array.

def remove_duplicates(arr):
    if len(arr) == 0:
        return 0

    # Pointer for the unique element
    unique_index = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]

    # Return the length of the array with unique elements
    return unique_index + 1

# Example usage
array_with_duplicates = [1, 1, 2, 3, 3, 4, 5, 5, 6]
new_length = remove_duplicates(array_with_duplicates)
print(f"Array after removing duplicates: {array_with_duplicates[:new_length]}")
