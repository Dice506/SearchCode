# Linear Search: This algorithm checks each element in the array one by one until it finds the target value.
# It works on both sorted and unsorted arrays but is not efficient for large datasets.

def linear_search(arr, target):
    # Loop through each element in the array
    for i in range(len(arr)):
        # If the current element matches the target, return its index
        if arr[i] == target:
            return i
    # If the target is not found, return -1
    return -1

# Example:
numbers = [10, 23, 45, 70, 11, 15]
target = 70

# Linear search to find the index of 70
index = linear_search(numbers, target)

# If target is found, print the index; otherwise, print not found
if index != -1:
    print(f"Target found at index {index}")
else:
    print("Target not found")

# Time Complexity: O(n) because in the worst case, it checks all elements.
# Linear Search is best when the array is small or unsorted.
