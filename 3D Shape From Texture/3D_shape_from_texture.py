#3D OBJECT FROM TEXTURE
import cv2
import numpy as np
import matplotlib.pyplot as plt

def estimate_3d_shape_from_texture(texture_image):
    
    gray = cv2.cvtColor(texture_image, cv2.COLOR_BGR2GRAY)
    gradient_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    gradient_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    gradient_z = np.ones_like(gradient_x)
    surface_normals = np.dstack((gradient_x, gradient_y, gradient_z))
    surface_normals /= np.linalg.norm(surface_normals, axis=-1, keepdims=True)
    return surface_normals
    
if __name__ == "__main__":
   
    texture_image = cv2.imread('/content/OCTA.png')
    texture_image = cv2.cvtColor(texture_image, cv2.COLOR_BGR2RGB)
    estimated_3d_shape = estimate_3d_shape_from_texture(texture_image)
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(texture_image)
    plt.axis("off")
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(estimated_3d_shape)
    plt.axis("off")
    plt.title('Estimated 3D Shape')

    plt.show()

