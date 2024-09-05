# Binary Search: This algorithm is more efficient than Linear Search but only works on sorted arrays.
# It divides the array into halves and checks which half the target belongs to, reducing the search space significantly.

def binary_search(arr, target):
    # Initialize low and high pointers
    low = 0
    high = len(arr) - 1

    # Loop while low is less than or equal to high
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Target found, return its index
        # If target is greater, search in the right half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, search in the left half
        else:
            high = mid - 1

    # Return -1 if the target is not found
    return -1

# Example:
sorted_numbers = [10, 15, 23, 45, 70, 85]
target = 23

# Binary search to find the index of 23
index = binary_search(sorted_numbers, target)

# If target is found, print the index; otherwise, print not found
if index != -1:
    print(f"Target found at index {index}")
else:
    print("Target not found")

# Time Complexity: O(log n) because the array is halved at each step.
# Binary Search is best for large, sorted arrays where efficient searching is needed.