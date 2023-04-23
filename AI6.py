# Recognize faces from the image -------

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image, convert it into a gray image, and show it
image=cv2.imread('people.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray,cmap='gray'),plt.show()

# Convert image to RGB image
def convertToRGB(image):
  return cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# Call the facial recognition database
face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# Detect faces in the frame
face_coo = face.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
print('Faces found :',len(face_coo))

for(x_face,y_face,w_face,h_face) in face_coo:
  cv2.rectangle(image,(x_face,y_face),(x_face+w_face,y_face+w_face),(0,255,0),10) # Draw a rectangle on faces

plt.imshow(convertToRGB(image)),plt.show()