#1. Usins the Sobel filter,filter the image and display it.

#import requried library
import scipy.ndimage
from scipy import misc
import matplotlib.pyplot as plt
# reads a raccoon face
#image = misc.face()
image = plt.imread('C:/Users/Kiran/Downloads/dog.jpg')

# Apply Sobel Filter
sobel_filtered_image = scipy.ndimage.filters.sobel(image)

# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(2, 1, figsize=(8, 8))

# The Original image
axis[0].imshow(image)
axis[0].set_title("The Original Picture")
axis[0].axis('off')

# The Sobel Filter
axis[1].imshow(sobel_filtered_image)
axis[1].set_title("The Sobel Filtered Picture")
axis[1].axis('off')

#show the filter
plt.show()