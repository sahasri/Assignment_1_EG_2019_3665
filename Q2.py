import cv2
import numpy as np
import matplotlib.pyplot as plt

# convert the image in to RGB colors
original_Image = cv2.cvtColor(cv2.imread('pic2.jpg'), cv2.COLOR_BGR2RGB)

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


fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0,0].imshow(original_Image)
axs[0,0].set_title("Original Image\n")
axs[0,1].imshow(spatial_ave_3x3)
axs[0,1].set_title("3X3 averaged Image\n")
axs[1,0].imshow(spatial_ave_10x10)
axs[1,0].set_title("10X10 averaged Image\n")
axs[1,1].imshow(spatial_ave_20x20)
axs[1,1].set_title("20X20 averaged Image\n")

plt.show()
