#use colab for execution
#IMAGE SEGMENTATION WITH WATERSHED ALGORITHM
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('/content/sample_data/DAMON SALVATORE.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
fig=plt.figure(dpi=300)
fig.add_subplot(3,3,1)
plt.imshow(image)
plt.axis("off")
plt.title('Original Image')
ret, threshold = cv2.threshold(gray, 0, 255,  cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
cv2.watershed(image, markers)
colored_markers = np.zeros_like(image)
colored_markers[markers == -1] = [255, 0, 0]  
segmented_image = cv2.addWeighted(image, 0.7, colored_markers, 0.3, 0)
fig.add_subplot(3,3,2)
plt.imshow(sure_bg)
plt.axis("off")
plt.title('Sure Background')

fig.add_subplot(3,3,3)
plt.imshow(dist_transform)
plt.axis("off")
plt.title('Distance Transform')
fig.add_subplot(3,3,4)

plt.imshow(sure_fg)
plt.axis("off")
plt.title('Sure Background')
fig.add_subplot(3,3,5)

plt.imshow(unknown)
plt.axis("off")
plt.title('Unknown')
fig.add_subplot(3,3,6)

plt.imshow(sure_bg)
plt.axis("off")
plt.title('Sure Background')
fig.add_subplot(3,3,7)

plt.imshow(markers)
plt.axis("off")
plt.title('Marker')
fig.add_subplot(3,3,8)

plt.imshow(colored_markers)
plt.axis("off")
plt.title('Colored Markers')
fig.add_subplot(3,3,9)

plt.imshow(segmented_image)
plt.axis("off")
plt.title('Segmented Image')
plt.show()
