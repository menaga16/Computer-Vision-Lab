#use colab for execution
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('/content/sample_data/elon musk.jpg', cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the RGB image to grayscale
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Sobel Edge Detection
sobel_x = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = np.sqrt(sobel_x**2 + sobel_y**2)

# Prewitt Edge Detection
prewitt_kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
prewitt_x = cv2.filter2D(image_gray, cv2.CV_64F, prewitt_kernel_x)
prewitt_y = cv2.filter2D(image_gray, cv2.CV_64F, prewitt_kernel_y)
prewitt_edges = np.sqrt(prewitt_x**2 + prewitt_y**2)

# Roberts Edge Detection
roberts_kernel_x = np.array([[1, 0], [0, -1]])
roberts_kernel_y = np.array([[0, 1], [-1, 0]])
roberts_x = cv2.filter2D(image_gray, cv2.CV_64F, roberts_kernel_x)
roberts_y = cv2.filter2D(image_gray, cv2.CV_64F, roberts_kernel_y)
roberts_edges = np.sqrt(roberts_x**2 + roberts_y**2)

# Canny Edge Detection
canny_edges = cv2.Canny(image_gray, 50, 150)

plt.figure(figsize=(10, 6))

plt.subplot(231), plt.imshow(image_rgb), plt.title('Original (RGB)')
plt.subplot(232), plt.imshow(sobel_edges, cmap='gray'), plt.title('Sobel')
plt.subplot(233), plt.imshow(prewitt_edges, cmap='gray'), plt.title('Prewitt')
plt.subplot(234), plt.imshow(roberts_edges, cmap='gray'), plt.title('Roberts')
plt.subplot(235), plt.imshow(canny_edges, cmap='gray'), plt.title('Canny')

plt.show()