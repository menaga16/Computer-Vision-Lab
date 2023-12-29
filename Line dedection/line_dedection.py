#use colab for execution
#LINE DETECTION USING HOUGH METHOD
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('/content/road.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
fig = plt.figure(dpi=300)
fig.add_subplot(1, 2, 1)
plt.imshow(image)
plt.axis("off")
plt.title('Original Image')

img_path = '/content/road.jpeg'
img = cv2.imread(img_path, 0)

if img is None:
    print(f"Error: Unable to load the image at {img_path}")
else:
    
    y, x = img.shape

    edges = cv2.Canny(img, x, y, apertureSize=3)

    lines_list = []
    lines = cv2.HoughLinesP(edges,1,np.pi / 180,threshold=40, minLineLength=5,maxLineGap=10)

    if lines is not None:

        for points in lines:
           
            x1, y1, x2, y2 = points[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            lines_list.append([(x1, y1), (x2, y2)])

        fig.add_subplot(1, 2, 2)
        plt.imshow(image)
        plt.axis("off")
        plt.title('Detected Lines')
        plt.show()
    else:
        print("No lines detected.")

