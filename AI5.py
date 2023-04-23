# Recognize shape from a photo (recognize the vehicles in the photo) -------


# import penCV و NumPy و Matplotlib و requests و PIL
import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image

# Read the image from a website and resize it
image = Image.open(requests.get('https://a57.foxnews.com/media.foxbusiness.com/BrightCove/854081161001/201805/2879/931/524/854081161001_5782482890001_5782477388001-vs.jpg', stream=True).raw)
image = image.resize((450,250))
image_arr=np.array(image)

# Convert image to gray image
grey = cv2.cvtColor(image_arr,cv2.COLOR_BGR2GRAY)

#Apply Gaussian Blur to the image in order to process the image and remove noise and blur 
blur = cv2.GaussianBlur(grey,(5,5),0)
Image.fromarray(blur)

# Expand the modified image by dilate and increase the size of the white areas
dilated = cv2.dilate(blur,np.ones((3,3)))
Image.fromarray(dilated)

# Create a kernel matrix of size (2, 2) on the image in order to prevent image erosion + fill parts of the image from the pixel
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
Image.fromarray(closing)

car_src = 'haarcascade_car.xml'
car = cv2.CascadeClassifier(car_src) # the function  to Read data
cars = car.detectMultiScale(closing, 1.1, 1) # The function used to identify shapes and objects

# count car in image
cnt = 0
for(x,y,w,h) in cars:
    cv2.rectangle(image_arr,(x,y),(x+w,y+h),(255,0,0),2) # Draw a rectangle on cars
cnt += 1
print(cnt,"CARS")
Image.fromarray(image_arr)

# Show image 
cv2.imshow('recognize the cars',image_arr)
cv2.waitKey()
cv2.destroyAllWindows()