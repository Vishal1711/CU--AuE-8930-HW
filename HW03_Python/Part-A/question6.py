import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Read the image.
img = cv2.imread('test_image.jpg')


bilateral = cv2.bilateralFilter(img, 5, 40, 100, borderType=cv2.BORDER_CONSTANT)



# Save the output.
cv2.imshow('test_image', img)
cv2.imshow('bilateral.jpg', bilateral)
cv2.imwrite('bilateral.jpg', bilateral) 
imag = mpimg.imread('test_image.jpg')
image = mpimg.imread('bilateral.jpg')
print(img)
print('-------------------------------------')
print(image)
cv2.waitKey(0)
