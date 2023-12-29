#use colab for execution
#OPENING AND CLOSING
import matplotlib.pyplot as plt
def opening(image, se):
    eroded = erosion(image, se)
    opened = dilation(eroded, se)
    return opened
def closing(image, se):
    dilated = dilation(image, se)
    closed = erosion(dilated, se)
    return closed
image = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 255, 0, 255, 0, 255, 0],
    [0, 0, 255, 255, 255, 0, 0],
    [0, 255, 0, 255, 0, 255, 0],
    [0, 0, 255, 255, 255, 0, 0],
    [0, 255, 0, 0, 0, 255, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
se = [
    [0, 255, 0],
    [255, 255, 255],
    [0, 255, 0]
]
opened_image = opening(image, se)
closed_image = closing(image, se)
fig = plt.figure(dpi=300)
fig.add_subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.axis("off")
plt.title("Original Image")
fig.add_subplot(1, 3, 2)
plt.imshow(opened_image, cmap='gray')
plt.axis("off")
plt.title("Opened Image")
fig.add_subplot(1, 3, 3)
plt.imshow(closed_image, cmap='gray')
plt.axis("off")
plt.title("Closed Image")
plt.show()

