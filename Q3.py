import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
original_Image = cv2.cvtColor(cv2.imread('pic1.jpg'), cv2.COLOR_BGR2RGB)

def rotate_image(original_Image, angle):
    # Height and width of the image
    height, width = original_Image.shape[:2]
    # Center of the image
    center = (width / 2, height / 2)
    # Rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    # New size of the rotated image
    if angle <= 45:
        new_dimension=  int((height + width) / np.sqrt(2))
        rotation_matrix[0, 2] += (new_dimension / 2) - center[0]
        rotation_matrix[1, 2] += (new_dimension / 2) - center[1]
        rotated_image = cv2.warpAffine(original_Image, rotation_matrix, (new_dimension, new_dimension), flags=cv2.INTER_LINEAR)
    elif angle >= 45:
        rotation_matrix[0, 2] += (height / 2) - center[0]
        rotation_matrix[1, 2] += (width / 2) - center[1]
        # Rotate the image without cropping the corners
        rotated_image = cv2.warpAffine(original_Image, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR)
    return rotated_image

# Rotate the image by 45 degrees
rotated_image_45 = rotate_image(original_Image, 45)

# Rotate the image by 90 degrees
rotated_image_90 = rotate_image(original_Image, 90)

# Display the images
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Display the 45 rotated image in the first subplot
ax1.imshow(rotated_image_45)
ax1.set_title("Image rotated by 45 degrees\n")

# Display the 90 rotated image in the second subplot
ax2.imshow(rotated_image_90)
ax2.set_title("Image rotated by 90 degrees\n")

plt.show()
