import cv2
import numpy as np
import matplotlib.pyplot as plt
# convert the image in to Grayscale
original_Image = cv2.imread('Image1.jpg',cv2.IMREAD_GRAYSCALE)
# convert the image in to RGB colors
#original_Image = cv2.cvtColor(cv2.imread('Image1.jpg'), cv2.COLOR_BGR2RGB)

def spatial_average(size,image):
    # Define the kernel for spatial averaging
    kernel=np.full((size, size), 1/(size * size))
    # Apply spatial averaging using the defined kernel
    average_image= cv2.filter2D(image, -1, kernel)
    return average_image


# Perform spatial averaging for different neighborhood sizes
spatial_ave_3x3= spatial_average(3,original_Image)
spatial_ave_10x10= spatial_average(10,original_Image)
spatial_ave_20x20= spatial_average(20,original_Image)


fig, axs = plt.subplots(2, 2, figsize=(7, 12))
axs[0,0].imshow(original_Image, cmap='gray')
axs[0,0].set_title("Original Image\n")
axs[0,1].imshow(spatial_ave_3x3, cmap='gray')
axs[0,1].set_title("3X3 averaged Image\n")
axs[1,0].imshow(spatial_ave_10x10, cmap='gray')
axs[1,0].set_title("\n\n10X10 averaged Image\n")
axs[1,1].imshow(spatial_ave_20x20, cmap='gray')
axs[1,1].set_title("\n\n20X20 averaged Image\n")

plt.show()
