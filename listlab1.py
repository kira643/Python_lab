# Write a Python program to sum all the items in a list.
def sum_list(items):
    total = 0
    for item in items:
        total += item
    return total

# Example usage
numbers = [5, 9, 18, 7, 5]
print("Sum of all items in the list:", sum_list(numbers))

# Output : Sum of all items in the list: 44