#2.Using SciPy Linear Algebra please solve the below problem. Input: 7x + 2y = 8 4x + 5y = 10

#import requried library
import numpy as np
from scipy import linalg

#crate given input array
arr =np.array(
[
[7, 2],
[4, 5]
]
)

#display the units of the input
units=np.array([8,10])

#use scipy linear algebra function
mix=linalg.solve(arr,units)

#print the values
print(mix)


#output:

#[0.74074074 1.40740741]
