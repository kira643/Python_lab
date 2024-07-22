#2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

#improt the requried liabrary
import numpy as np

#create a array of ranging from 2 to 10.
arr = np.array([2,3,4,5,6,7,8,9,10])

#create a 3x3 matrix
matrix = arr.reshape(3,3)

#print original array
print("Original_array:",arr)

#print 3x3 reshape matrix
print(matrix)

#o/p:
#Original_array: [ 2  3  4  5  6  7  8  9 10]
#[[ 2  3  4]
 #[ 5  6  7]
 #[ 8  9 10]]