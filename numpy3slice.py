#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives


#improt the requried liabrary
import numpy as np

# Create an array of 10 zeros
arr1 = np.array([0,0,0,0,0,0,0,0,0,0])

# Create an array of 10 ones
arr2 = np.array([1,1,1,1,1,1,1,1,1,1])

# Create an array of 10 fives
arr3 = np.array(arr2) * 5

#print the output
print("Array of 10 zeros:" , arr1)#output=[0 0 0 0 0 0 0 0 0 0]
print("Array of 10 ones:" , arr2)#output=[1 1 1 1 1 1 1 1 1 1]
print("Array of 10 fives:" , arr3)#output=[5 5 5 5 5 5 5 5 5 5]

#o/p:
#Array of 10 zeros: [0 0 0 0 0 0 0 0 0 0]
#Array of 10 ones: [1 1 1 1 1 1 1 1 1 1]
#Array of 10 fives: [5 5 5 5 5 5 5 5 5 5]