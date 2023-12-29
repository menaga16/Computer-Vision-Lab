#use colab for execution
#BOUNDARY EXTRACTION
import numpy as np
# Original image and structuring element
image = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 255, 255, 255, 255, 255, 0],
    [0, 255, 255, 255, 255, 255, 0],
    [0, 255, 255, 255, 255, 255, 0],
    [0, 255, 255, 255, 255, 255, 0],
    [0, 255, 255, 255, 255, 255, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
se = [
    [0, 255, 0],
    [255, 255, 255],
    [0, 255, 0]
]
# Compute erosion
eroded_image = erosion(image, se)
# Compute boundary by subtracting eroded image from original image
boundary_image = np.subtract(image, eroded_image)
# Display the boundary image
fig = plt.figure(dpi=300)
fig.add_subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.axis("off")
plt.title("Original Image")
fig.add_subplot(1, 3, 2)
plt.imshow(se, cmap='gray')
plt.axis("off")
plt.title("Structuring Element")
fig.add_subplot(1, 3, 3)
plt.imshow(boundary_image, cmap='gray')
plt.axis("off")
plt.title("Boundary Image")
plt.show()

