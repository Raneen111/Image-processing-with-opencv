
# Recognize faces from a camera (real time )-------


# import openvv
import cv2

# Call the facial recognition database
face = cv2.CascadeClassifier('myfacedetector.xml')

# open the camera
camera = cv2.VideoCapture(0)

# cteate new window
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

# loop to read frame by frame in the video
while True:
    read_ok, frame = camera.read()

# If frame reading fails, the loop stops
    if not read_ok:
        break
    
     # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the frame
    faces = face.detectMultiScale(gray)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)  # Draw a rectangle on faces

   # Show image 
    cv2.imshow('frame', frame)


# If the letter "z" is pressed from the keyboard, the loop stops and the camera closes
    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

# Close the video file and close the viewing window
camera.release()
cv2.destroyAllWindows()