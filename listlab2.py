# Write a Python program to get the largest and smallest number from a list without builtin functions

def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None  # Return None if the list is empty

    # Initialize largest and smallest with the first element
    largest = smallest = numbers[0]

    # Iterate through the list to find the largest and smallest numbers
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example usage
numbers = [3, 5, 1, 8, 2, -4, 7]
largest, smallest = find_largest_and_smallest(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")


# Output :
          #  Largest number: 8
          #  Smallest number: -4