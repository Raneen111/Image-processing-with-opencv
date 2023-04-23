# Human, dog and cat recognition from a dataset + data training for recognition -----
#In order to train the data, follow the steps in the video from minute 1:5:00 (https://www.youtube.com/watch?v=OxTOzSr2NZ0)



#import NumPy , OpenCV and matplotlib
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load dog, human and cat recognition files and store them in separate variables
face_cascade=cv2.CascadeClassifier('mydogdetector.xml')
face_cascade2=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade3=cv2.CascadeClassifier('mycatdetector2.xml')

# Read the image, convert it into a gray image, and show it
img=cv2.imread('family.bmp')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Determine the type of font that will be used to write on the image
font=cv2.FONT_HERSHEY_SIMPLEX

# recognize the dogs, human, and cats in the images 
faces=face_cascade.detectMultiScale(gray,1.345,5,75)
faces2=face_cascade2.detectMultiScale(gray,1.3,5)
faces3=face_cascade3.detectMultiScale(gray,1.3,2,75)

# Draw a box around each dog discovered in the picture and write the word “dog” next to it
for(x,y,w,h) in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.putText(img,'Dog',(x,y),font,0.9,(0,255,0),2)

# Draw a square around each human being discovered in the picture and write the word "Human" next to it
for(z,v,b,n) in faces2:
	img=cv2.rectangle(img,(z,v),(z+b,v+n),(0,0,255),2)
	cv2.putText(img,'Human',(z,v),font,0.9,(0,0,255),2)

# Draw a square around each cat discovered in the image and write the word "Cat" next to it
for(q,w,e,r) in faces3:
	img=cv2.rectangle(img,(q,w),(q+e,w+r),(255,0,0),2)
	cv2.putText(img,'Cat',(q,w),font,0.9,(255,0,0),2)
	
#Change the order of the color channels in the image from BGR to RGB
p,l,m=cv2.split(img)
img=cv2.merge([m,l,p])

# Show image 
plt.imshow(img)
plt.show()

# Waiting to press any key on the keyboard to close open windows
cv2.waitKey(0)
cv2.destroyAllWindows()

