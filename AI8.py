# Open the camera -------


#import openCV
import cv2

# open the camera
camera = cv2.VideoCapture(0)

# loop to read frame by frame in the video
while(True):
    
    ret, frame = camera.read()

    #  Show frame video
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff == ord('s'):
        break

# Close the video file and close the viewing window
camera.release()
cv2.destroyAllWindows()