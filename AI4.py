#Detect the corner points in the image -------

#import openCV و NumPy و Matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt

##Read image from img.jpg file and store it as a variable image
img = cv2.imread("Tringle.jpg")

#Convert image to gray image
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

#Convert the gray image to float32 (array)
gray = np.float32(gray)

#Detect the corner points in the image  with the (Harris corner detector) Function 
des = cv2.cornerHarris(gray,2,5,0.07)

# Expand the detected angle that can be expanded
des = cv2.dilate(des,None)

## Change the color of detected corner points in the image to red
img[des>0.01 *des.max()]=[255,0,0]

# Show image
plt.imshow(img)


# Waiting to press any key on the keyboard to exit the image
plt.waitforbuttonpress()