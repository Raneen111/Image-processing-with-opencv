# convert image to gray image ----

#import OpenCV , NumPy and Matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Read image from img.jpg file and store it as a variable image
image = cv2.imread("img.jpg")

# Convert image to gray image
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

# Save the gray image in a new file named "Photo.jpg"
cv2.imwrite("Photo.jpg" , gray)

# Show image
cv2.imshow('Photo', gray)

I = cv2.waitKey(0)

## The window of the image will be closed if we press S or command Esc
if I == 27 or I == ord('S'):
    cv2.destroyAllWindows()
    
