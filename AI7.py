# Recognize faces from a Video -------


import cv2

# Call the facial recognition database
face_detector = cv2.CascadeClassifier('myfacedetector.xml') 

#  video call 
cape = cv2.VideoCapture('Elon Musk.mp4')

# Verify the success of opening the video file
if not cape.isOpened():
    print("Could not open video file")
    exit()



# loop to read frame by frame in the video
while True:
    
    ret, img = cape.read()
    if not ret:
        print("Could not read frame")
        break

# Convert frame to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Detect faces in the frame
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h),(255, 0, 0),5 ) # Draw a rectangle on faces

    # Show image 
    cv2.imshow('Video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Close the video file and close the viewing window
cape.release()
cv2.destroyAllWindows()