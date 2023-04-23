# Detect the corner points in the text ----

# import openCV و NumPy و Matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image from img.jpg file and store it as a variable image
img = cv2.imread("Text.jpg")

# Convert image to gray image
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

# show image
plt.imshow(img),plt.show()

# Detect the corner points in the text with the (goodFeaturesToTrack) Function 
corner=cv2.goodFeaturesToTrack(gray, 30, 0.01, 10)
corner=np.int0(corner)

for i in corner :
    x, y =i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)  # Draw corners on the text ( 3=radius, 255 color , -1 circle thickness)


# Show image
plt.imshow(img)
# Waiting to press any key on the keyboard to exit the image
plt.waitforbuttonpress()