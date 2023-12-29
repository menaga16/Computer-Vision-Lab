#use colab for execution
#DILATION AND EROSION
import matplotlib.pyplot as plt
def erosion(image, se):
    m, n = len(image), len(image[0])
    result = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            min_val = 255
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if se[k + 1][l + 1] == 255:
                        min_val = min(min_val, image[i + k][j + l])
            result[i][j] = min_val
    return result
def dilation(image, se):
    m, n = len(image), len(image[0])
    result = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            max_val = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if se[k + 1][l + 1] == 255:
                        max_val = max(max_val, image[i + k][j + l])
            result[i][j] = max_val
    return result
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
eroded_image = erosion(image, se)
dilated_image = dilation(image, se)
fig = plt.figure(dpi=300)
fig.add_subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.axis("off")
plt.title("Original Image")
fig.add_subplot(2, 2, 2)
plt.imshow(se, cmap='gray')
plt.axis("off")
plt.title("Structuring Element")
fig.add_subplot(2, 2, 3)
plt.imshow(eroded_image, cmap='gray')
plt.axis("off")
plt.title("Eroded Image")
fig.add_subplot(2, 2, 4)
plt.imshow(dilated_image, cmap='gray')
plt.axis("off")
plt.title("Dilated Image")
plt.show()

