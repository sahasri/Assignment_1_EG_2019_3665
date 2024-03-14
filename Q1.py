import cv2
import numpy as np
import matplotlib.pyplot as plt
# convert the image in to Grayscale
original_Image = cv2.imread('Image1.jpg', cv2.IMREAD_GRAYSCALE)
# convert the image in to RGB colors
#original_Image = cv2.cvtColor(cv2.imread('pic1.jpg'), cv2.COLOR_BGR2RGB)
# Get desired number of intensity levels from user and handling invalid inputs
for _ in iter(int, 1):
    try:
        intensity_levels = int(input("Enter the desired number of intensity levels from 1 to 8= "))
        if 1 <= intensity_levels <= 8:
            break
        else:
            print("Entered value is not between 1 and 8. Try again")
    except ValueError:
        print("Invalid input. Please enter an integer.")


def reduce_levels(image, intensity_levels):
    # Normalize the image to the range [0, 1]
    normalized_image = (image + 1) / 256
    # Adjust the intensity levels
    adjusted_image = np.round(normalized_image * (2 ** intensity_levels)) / (2 ** intensity_levels)
    # Denormalize the image back to the original range
    denormalized_image = adjusted_image * 256 - 1
    # Round the pixel values and ensure there are in range of uint8
    reduced_image = np.round(denormalized_image).astype(np.uint8)
    return reduced_image

# Call function for reduce intensity levels
adjusted_Image = reduce_levels(original_Image,intensity_levels)
# Show the image
fig, axs = plt.subplots(1, 2, figsize=(12,6))
# Display the original image in the first subplot
axs[0].imshow(original_Image,cmap="gray")
axs[0].set_title("Original image\n")
# Display the reduced intensity image in the second subplot
axs[1].imshow(adjusted_Image,cmap="gray")
axs[1].set_title("Image with 2^{} intensity levels\n".format(intensity_levels))

plt.show()
