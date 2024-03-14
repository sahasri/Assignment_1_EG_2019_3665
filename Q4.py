import cv2
import numpy as np
import matplotlib.pyplot as plt

def average_blocks(image, block_size):

    # Get the height and width of the image
    height, width = image.shape[:2]
    # Create a new array for the result with the same dimensions as the original image
    result = np.zeros_like(image)
    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            # Extract the current block
            block = image[i:i+block_size, j:j+block_size]
            # Calculate the average pixel value
            avg = np.mean(block, axis=(0,1))
            # Fill the current block with the average pixel value
            result[i:i+block_size, j:j+block_size] = avg

    return result

# Load the original image
original_image = cv2.imread('Image1.jpg',cv2.IMREAD_GRAYSCALE)

# Get the shape of the original image
image_shape = original_image.shape

# Create output images with corresponding sizes
replaced_3x3 = np.zeros_like(original_image)
replaced_5x5 = np.zeros_like(original_image)
replaced_7x7 = np.zeros_like(original_image)

# Averaging 3x3 block
replaced_3x3 = average_blocks(original_image, 3)
# Averaging 5x5 block
replaced_5x5 = average_blocks(original_image, 5)
# Averaging 7x7 block
replaced_7x7 = average_blocks(original_image, 7)

# Plot the original and downscaled images
fig, axs = plt.subplots(2, 2, figsize=(7,12))
axs[0,0].imshow(original_image,  cmap='gray')
axs[0,0].set_title("Original image\n")
axs[0,1].imshow(replaced_3x3,cmap='gray')
axs[0,1].set_title("Image downscaled by 3x3\n")
axs[1,0].imshow(replaced_5x5,cmap='gray')
axs[1,0].set_title("Image downscaled by 5x5\n")
axs[1,1].imshow(replaced_7x7, cmap='gray')
axs[1,1].set_title("Image downscaled by 7x7\n")
plt.show()
